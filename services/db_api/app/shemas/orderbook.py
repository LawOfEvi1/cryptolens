from pydantic import BaseModel

class MaximumOrderBookLimitsIn(BaseModel):
    symbol: str
    delta_count_coin: float
    max_buyers_price: float
    max_buyers_coin: float
    max_sellers_price: float
    max_sellers_coin: float
    average_price: float
    timestamp_ms: float
