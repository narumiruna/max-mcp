from .client import MAXRestClient
from .types import Market


class MAXExchange:
    def __init__(self) -> None:
        self.client = MAXRestClient()

    async def get_markets(self) -> list[Market]:
        """
        Get all available markets.

        Returns:
            list[Market]: A list of available markets.
        """
        data = await self.client.make_request("/api/v3/markets")
        return [Market.model_validate(d) for d in data]

    async def get_index_price(self, symbol: str) -> float:
        data = await self.get_all_index_prices()
        return data[symbol]

    async def get_all_index_prices(self) -> dict[str, float]:
        """Get latest index prices of m-wallet

        Returns:
            dict[str, float]: A dictionary containing market id(symbol) as key and index price as value.
        """
        resp = await self.client.make_request("/api/v3/wallet/m/index_prices")
        return {k: float(v) for k, v in resp.items()}
