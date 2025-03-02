from .server import serve


def main():
    """MCP xcodebuild Server - Building iOS Xcode workspace/project"""
    import asyncio
    asyncio.run(serve())


if __name__ == "__main__":
    main()