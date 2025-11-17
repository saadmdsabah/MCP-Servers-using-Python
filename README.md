# FastMCP & FastAPI-MCP Examples

This repository is a collection of sample projects and practice files demonstrating how to build [Model Context Protocol (MCP)](https://fastmcp.dev/) servers using both the `fastmcp` (pure) and `fastapi_mcp` (FastAPI integration) libraries.

It includes examples for:
* Wrapping a pure function (`calculator.py`)
* Wrapping an external API (`weather.py`)
* Parsing an RSS feed (`GoogleFeedParser.py`)
* Auto-generating tools from a full FastAPI API (`calculator-api.py`)

---

## 🚀 Live Deployed Server: Google News Parser

The code from `GoogleFeedParser.py` (also organized in the `MCP Deployment using FastMCP Cloud` folder) is deployed as a live, public MCP server.

* **Live MCP Endpoint:** `https://google-news-parser.fastmcp.app/mcp`
* **Deployment-Specific Repo:** More information about this specific deployment can be found at: [https://github.com/saadmdsabah/Google-News-Parser-MCP-server](https://github.com/saadmdsabah/Google-News-Parser-MCP-server)

### Quick Usage

#### 1. Using Cursor.ai
Create an `mcp.json` file in your project's root:
 ```json
      {
          "mcpServers": {
              "google-news-parse": {
                  "url": "https://google-news-parser.fastmcp.app/mcp"
              }
          }
      }
 ```
