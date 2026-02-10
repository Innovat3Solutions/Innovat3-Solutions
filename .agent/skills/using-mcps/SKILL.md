---
name: using-mcps
description: Guide for using and installing Model Context Protocol (MCP) servers for Magic UI, Supabase, GoHighLevel, and Firecrawl.
---

# Using MCPs (Model Context Protocol)

This skill provides a knowledge base for utilizing various MCP servers to enhance your coding and development workflow. MCP servers allow AI agents (like Claude or Cursor) to communicate with external tools and data sources.

## When to Use This Skill
- When you need to install or configure a new MCP server.
- When you want to generate UI components using Magic UI.
- When you need to interact with a Supabase database.
- When you need to manage GoHighLevel sub-accounts.
- When you need to scrape websites using Firecrawl.

## MCP Server List & installation

### 1. Magic UI
**Description**: Allows searching and installing Magic UI components directly into your project.
**Usage**: "Add the Magic UI Bento Grid component."

**Installation (Claude Desktop / Cursor):**
Add the following to your MCP configuration file:

```json
{
  "mcpServers": {
    "magicui": {
      "command": "npx",
      "args": [
        "-y",
        "@magicuidesign/mcp"
      ]
    }
  }
}
```

### 2. Supabase
**Description**: Interact with your Supabase project (database, auth, etc.).
**Usage**: "Query the 'users' table in my Supabase project."

**Installation:**
There are two main ways to use Supabase with MCP:

**A. Local Development (Recommended for active dev)**
1. Ensure the Supabase CLI is installed (`npm i -g supabase` or `brew install supabase/tap/supabase`).
2. Run `supabase start` in your project.
3. The MCP server is exposed at `http://localhost:54321/mcp`.
4. Configure your client to use this SSE (Server-Sent Events) endpoint.

**B. Community Server (Node.js)**
Use the community-maintained server.

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp"], 
      "env": {
        "SUPABASE_URL": "your-project-url",
        "SUPABASE_SERVICE_ROLE_KEY": "your-service-role-key"
      }
    }
  }
}
```
*(Note: Verify package name `@supabase/mcp` on npm or use `npx @modelcontextprotocol/server-supabase` if available. Often cloning the repo is required for some community servers involved in rapid dev).*

### 3. Firecrawl
**Description**: Turn websites into LLM-ready markdown.
**Usage**: "Scrape https://example.com and give me the content."

**Installation:**

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": [
        "-y",
        "firecrawl-mcp"
      ],
      "env": {
        "FIRECRAWL_API_KEY": "your-firecrawl-api-key"
      }
    }
  }
}
```

### 4. GoHighLevel
**Description**: Manage GoHighLevel locations, contacts, and opportunities.
**Usage**: "Get details for contact ID 123 in GHL."

**Installation:**
Using the `knotie-ai-mcp` or similar community package.

```json
{
  "mcpServers": {
    "gohighlevel": {
      "command": "npx",
      "args": [
        "-y",
        "knotie-ai-mcp"
      ],
      "env": {
        "GHL_API_KEY": "your-ghl-private-api-key",
        "GHL_LOCATION_ID": "your-location-id"
      }
    }
  }
}
```

## How to Configure

### Claude Desktop
Edit `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS (or `%APPDATA%\Claude\claude_desktop_config.json` on Windows) and add the JSON snippets above to the `"mcpServers"` object.

### Cursor
Go to **Settings > Features > MCP** (or similar, depending on version) and add the servers. For `npx` commands, you may need to specify the absolute path to your node executable or ensure `npx` is in the path.

### General Tips
- **Restart**: Always restart your MCP client (Claude App, Cursor) after editing the config.
- **API Keys**: more secure to use an `.env` file if supported, or passing them directly in the config as shown above (be careful with sharing config files).
