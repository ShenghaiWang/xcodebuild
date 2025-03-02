from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    ErrorData,
    TextContent,
    Tool,
    Annotations,
    Field,
    Annotated,
    INVALID_PARAMS,
)
from pydantic import BaseModel
import subprocess
import os, json
from mcp.shared.exceptions import McpError


def find_xcode_project():
    for root, dirs, files in os.walk("."):
        dirs.sort(reverse = True)
        for dir in dirs:
            if dir.endswith(".xcworkspace") or dir.endswith(".xcodeproj"):
                return os.path.join(root, dir)
    return None

def find_scheme(project_type: str, project_name: str) -> str:
    schemes_result = subprocess.run(["xcodebuild",
                                    "-list",
                                    project_type,
                                    project_name],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    check=False).stdout.decode("utf-8")
    
    schemes_lines = schemes_result.splitlines()
    schemes = []
    in_schemes_section = False
    for line in schemes_lines:
        if "Schemes:" in line:
            in_schemes_section = True
            continue
        if in_schemes_section:
            scheme = line.strip()
            if scheme:
                schemes.append(scheme)
    
    if schemes:
        return schemes[0]
    else:
        return ""

def find_available_simulator() -> str:
    devices_result = subprocess.run(["xcrun", "simctl", "list", "devices", "--json"], stdout=subprocess.PIPE, check=False)
    devices_json = json.loads(devices_result.stdout.decode("utf-8"))
    
    for runtime_id, devices in devices_json["devices"].items():
        if "iOS" in runtime_id:
            for device in devices:
                if device["isAvailable"]:
                    return f'platform=iOS Simulator,name={device["name"]},OS={runtime_id.split(".")[-1].replace("iOS-", "").replace("-", ".")}'
    return ""
class Folder(BaseModel):
    """Parameters"""
    folder: Annotated[str, Field(description="The full path of the current folder that the iOS Xcode workspace/project sits")]

async def serve() -> None:
    server = Server("build")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name = "build",
                description = "Build the iOS Xcode workspace/project in the folder",
                inputSchema = Folder.model_json_schema(),
            ),
            Tool(
                name="test",
                description="Run test for the iOS Xcode workspace/project in the folder",
                inputSchema=Folder.model_json_schema(),
            )
        ]

    @server.call_tool()
    async def call_tool(name, arguments: dict) -> list[TextContent]:
        try:
            args = Folder(**arguments)
        except ValueError as e:
            raise McpError(ErrorData(code=INVALID_PARAMS, message=str(e)))

        os.chdir(args.folder)
        xcode_project_path = find_xcode_project()

        project_type = ""
        project_name = ""
        if xcode_project_path.endswith(".xcworkspace"):
            project_type = "-workspace"
            project_name = os.path.basename(xcode_project_path)
        else:
            project_type = "-project"
            project_name = os.path.basename(xcode_project_path)
    
        scheme = find_scheme(project_type, project_name)
        destination = find_available_simulator()
        command = ["xcodebuild",
                   project_type,
                   project_name,
                   "-scheme",
                   scheme,
                   "-destination",
                   destination]
        if name == "build":
            result = subprocess.run(command, stdout=-1, check=False).stdout
        else:
            result = subprocess.run(command + ["test"], stdout=subprocess.PIPE, check=False).stdout
        
        lines = result.decode("utf-8").splitlines()
        error_lines = [line for line in lines if "error:" in line.lower()]
        error_message = "\n".join(error_lines)
        if not error_message:
            error_message = "Successful"

        return [TextContent(type="text", text=f"{error_message}")]

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options, raise_exceptions=True)

if __name__ == "__main__":
    import asyncio
    asyncio.run(serve())
