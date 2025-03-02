# xcodebuild MCP Server

A Model Context Protocol server that builds iOS workspace/project that enables seamless workflow working with iOS projects in Visual Studio Code using extensions like Cline or Roo Code.

### Available Tools

- `build` - Build iOS Xcode workspace/project
    - `folder` (string, required): The full path of the current folder that the iOS Xcode workspace/project sits
- `test` - Run test for iOS Xcode workspace/project
    - `folder` (string, required): The full path of the current folder that the iOS Xcode workspace/project sits

## Installation


### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *xcodebuild*.

### Using PIP

Alternatively you can install `xcodebuild` via pip:

```
pip install xcodebuild
```

After installation, you can run it as a script using:

```
python -m  xcodebuild
```

## Configuration

### Configure for Claude.app

Add to your Claude settings:

<details>
<summary>Using uvx</summary>

```json
"mcpServers": {
  "xcodebuild": {
    "command": "uvx",
    "args": ["xcodebuild"]
  }
}
```
</details>

<details>
<summary>Using pip installation</summary>

```json
"mcpServers": {
  "xcodebuild": {
    "command": "python",
    "args": ["-m", "xcodebuild"]
  }
}
```
</details>


## License

xcodebuild MCP tool is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.