from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from .exchange import MAXExchange

exchange = MAXExchange()

# https://github.com/jlowin/fastmcp/issues/81#issuecomment-2714245145
mcp = FastMCP("MCP Server MAX", log_level="ERROR")


@mcp.tool()
async def get_markets() -> str:
    """Get all available markets."""
    markets = await exchange.get_markets()
    return "\n".join(str(market) for market in markets)


def main():
    mcp.run()
