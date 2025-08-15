# xcodebuild MCP Server

A Model Context Protocol server that builds iOS workspace/project that enables seamless workflow working with iOS projects in Visual Studio Code using extensions like Cline or Roo Code.

[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/ShenghaiWang/xcodebuild)](https://archestra.ai/mcp-catalog/shenghaiwang__xcodebuild)
<a href="https://glama.ai/mcp/servers/5ibnbzxmql">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/5ibnbzxmql/badge" alt="mcpxcodebuild MCP server" />
</a>

### Available Tools

- `build` - Build iOS Xcode workspace/project
    - `folder` (string, required): The full path of the current folder that the iOS Xcode workspace/project sits
- `test` - Run test for iOS Xcode workspace/project
    - `folder` (string, required): The full path of the current folder that the iOS Xcode workspace/project sits

## Installation


### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcpxcodebuild*.

### Using PIP

Alternatively you can install `mcpxcodebuild` via pip:

```
pip install mcpxcodebuild
```

After installation, you can run it as a script using:

```
python -m  mcpxcodebuild
```

## Configuration

### Configure for Claude.app

Add to your Claude settings:

<details>
<summary>Using uvx</summary>

```json
"mcpServers": {
  "mcpxcodebuild": {
    "command": "uvx",
    "args": ["mcpxcodebuild"]
  }
}
```
</details>

<details>
<summary>Using pip installation</summary>

```json
"mcpServers": {
  "mcpxcodebuild": {
    "command": "python",
    "args": ["-m", "mcpxcodebuild"]
  }
}
```
</details>


## License

xcodebuild MCP tool is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.