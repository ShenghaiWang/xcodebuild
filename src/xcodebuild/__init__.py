from .server import serve


def main():
    """MCP xcodebuild Server - Building iOS Xcode workspace/project"""
    import asyncio
    asyncio.run(serve(args.user_agent, args.ignore_robots_txt))


if __name__ == "__main__":
    main()