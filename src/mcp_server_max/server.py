from mcp.server.fastmcp import FastMCP

from .exchange import MAXExchange

exchange = MAXExchange()

# https://github.com/jlowin/fastmcp/issues/81#issuecomment-2714245145
mcp = FastMCP("MCP Server MAX", log_level="ERROR")


@mcp.tool()
async def get_markets() -> str:
    """Retrieve all available markets on the MAX exchange.

    This function fetches comprehensive information about all markets on the MAX exchange,
    including trading pairs, status, precision, and minimum trading amounts.

    Returns:
        str: A formatted string containing details of all markets, with each market on a new line.
            Information includes market ID, status, base and quote units, precision values,
            minimum amounts, and m-wallet support status.

    Example:
        ```python
        markets = await get_markets()
        print(markets)
        ```
        Output:
        ```
        Market: id='maxtwd' status='active' base_unit='max' base_unit_precision=2 min_base_amount=22.1 quote_unit='twd' quote_unit_precision=4 min_quote_amount=250.0 m_wallet_supported=False
        Market: id='btctwd' status='active' base_unit='btc' base_unit_precision=8 min_base_amount=8e-05 quote_unit='twd' quote_unit_precision=1 min_quote_amount=250.0 m_wallet_supported=True
        Market: id='ethtwd' status='active' base_unit='eth' base_unit_precision=6 min_base_amount=0.0035 quote_unit='twd' quote_unit_precision=1 min_quote_amount=250.0 m_wallet_supported=True
        ```
    """  # noqa: E501
    markets = await exchange.get_markets()
    return "\n".join(str(market) for market in markets)


def main():
    mcp.run()
