from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from mcp_server_max.v3.
# https://github.com/jlowin/fastmcp/issues/81#issuecomment-2714245145
mcp = FastMCP("MCP Server MAX", log_level="ERROR")


@mcp.tool()
def add_numbers(
    a: Annotated[float, Field(description="The first number")],
    b: Annotated[float, Field(description="The second number")],
) -> str:
    """Add two numbers and return the result as a string."""
    return f"{a} + {b} = {a+b} from MCP MAX"


def main():
    mcp.run()
