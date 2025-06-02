from pydantic import BaseModel

class LiquidationIn(BaseModel):
    symbol: str
    timestamp_ms: float
    type: str
    volume: float
    price: float
