from pydantic import BaseModel

class KlineIn(BaseModel):
    symbol: str
    start: int
    end: int
    interval: str
    open: float
    close: float
    high: float
    low: float
    volume: float
    turnover: float
