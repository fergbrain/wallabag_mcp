# wallabag-mcp

An MCP (Model Context Protocol) server that exposes your self-hosted [Wallabag](https://wallabag.org) instance to Claude and other MCP clients.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) for dependency management
- A running Wallabag instance with API access enabled

## Setup

### 1. Clone and install dependencies

```bash
git clone <repo-url>
cd wallabag_mcp
uv sync
```

### 2. Get Wallabag API credentials

In your Wallabag instance:

1. Go to **Settings → API clients management**
2. Click **Create a new client**
3. Note the **Client ID** and **Client Secret**

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
WALLABAG_BASE_URL=https://your-wallabag-instance.com
WALLABAG_CLIENT_ID=your_client_id
WALLABAG_CLIENT_SECRET=your_client_secret
WALLABAG_USERNAME=your_wallabag_username
WALLABAG_PASSWORD=your_wallabag_password
```

## Using with Claude Desktop

Add the following to your Claude Desktop config file.

**Config file location:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "wallabag": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ABSOLUTE/PATH/TO/wallabag_mcp",
        "python",
        "src/server.py"
      ],
      "env": {
        "PYTHONPATH": "/ABSOLUTE/PATH/TO/wallabag_mcp/src",
        "WALLABAG_BASE_URL": "https://your-wallabag-instance.com",
        "WALLABAG_CLIENT_ID": "your_client_id",
        "WALLABAG_CLIENT_SECRET": "your_client_secret",
        "WALLABAG_USERNAME": "your_wallabag_username",
        "WALLABAG_PASSWORD": "your_wallabag_password"
      }
    }
  }
}
```

Replace `/ABSOLUTE/PATH/TO/wallabag_mcp` with the actual path, e.g. `/Users/yourname/Projects/wallabag_mcp`.

After editing the config, restart Claude Desktop. You should see the Wallabag tools available in the tools menu.

## Available tools

| Tool | Description |
|------|-------------|
| `get_wallabag_articles` | Fetch saved articles with optional filters (archived, domain, date range, count, sort order) |
| `get_single_wallabag_article` | Fetch a single article by its ID |
| `search_articles` | Search articles by keyword |

### Example prompts

- *"What are my last 10 saved articles?"*
- *"Show me unread articles from the last 7 days"*
- *"Find my saved articles about Python"*
- *"Get article 42 with full content"*

## Running tests

```bash
uv run pytest
```

## Running the server directly

```bash
PYTHONPATH=src uv run python src/server.py
```

## Known limitations

- Authentication tokens are not automatically refreshed. If a token expires (typically after 1 hour), restart the server or reconnect from the client.
