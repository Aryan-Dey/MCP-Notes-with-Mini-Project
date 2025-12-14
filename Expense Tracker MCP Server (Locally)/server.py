# Converting FastAPI to FastMCP Server - We can use FastAPI to build the API and then convert it to FastMCP Server
from fastmcp import FastMCP
from main import app

mcp = FastMCP.from_fastapi(
    app = app,
    name = "Expense Tracker MCP Server",
)

if __name__ == "__main__":
    mcp.run()