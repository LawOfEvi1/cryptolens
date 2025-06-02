from pydantic import BaseModel

class VolumeMotionIn(BaseModel):
    symbol: str
    timestamp_ms: float
    delta: float
    delta_min: float
    delta_max: float
    bids: float
    asks: float
    price: float
    start: bool
    end: bool
    trend: str
