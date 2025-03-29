from datetime import datetime
from typing import Literal

from pydantic import BaseModel
from pydantic import field_validator

OrderType = Literal["market", "limit", "stop_market", "stop_limit", "post_only", "ioc_limit"]
# {
# "id": 87,
# "wallet_type": "m",
# "market": "ethtwd",
# "client_oid": "4511dc1f-4b28-4adb-a384-109384d3bc6e",
# "group_id": 1,
# "side": "buy",
# "state": "wait",
# "ord_type": "limit",
# "price": "21499.0",
# "stop_price": "21499.0",
# "avg_price": "21499.0",
# "volume": "0.2658",
# "remaining_volume": "0.2658",
# "executed_volume": "0.0",
# "trades_count": 0,
# "created_at": 1521726960123,
# "updated_at": 1521726960123
# }


class Order(BaseModel):
    id: int
    wallet_type: str
    market: str
    client_oid: str | None
    group_id: int | None
    side: str
    state: str
    ord_type: OrderType
    price: float | None
    stop_price: float | None
    avg_price: float | None
    volume: float | None
    remaining_volume: float | None
    executed_volume: float | None
    trades_count: int | None
    created_at: datetime | None
    updated_at: datetime | None

    @field_validator("created_at", "updated_at", mode="before")
    @classmethod
    def convert_datetime(cls, value: int | None) -> datetime | None:
        if value is None:
            return None

        print(value)
        return datetime.fromtimestamp(int(value / 1000))

    @field_validator("price", "stop_price", "avg_price", "remaining_volume", "executed_volume", mode="before")
    @classmethod
    def convert_float(cls, value: str | float | None) -> float | None:
        if value is None:
            return None

        if isinstance(value, str):
            return float(value)

        return value
