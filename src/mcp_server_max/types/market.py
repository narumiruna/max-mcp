from pydantic import BaseModel


class Market(BaseModel):
    id: str
    status: str
    base_unit: str
    base_unit_precision: int
    min_base_amount: float
    quote_unit: str
    quote_unit_precision: int
    min_quote_amount: float
    m_wallet_supported: bool
