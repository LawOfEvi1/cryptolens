from sqlalchemy import Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import MappedColumn, Mapped
from db.models.BaseORMModel import BaseORMModel  # базовый класс с методами

class VolumeMotion(BaseORMModel):
    __tablename__ = 'volume_motion'

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)
    symbol: Mapped[str] = MappedColumn(String, ForeignKey("trading_pair.symbol"), nullable=False)
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger, nullable=False)

    delta: Mapped[float]
    delta_min: Mapped[float]
    delta_max: Mapped[float]
    bids: Mapped[float]
    asks: Mapped[float]
    price: Mapped[float]
    start: Mapped[bool]
    end: Mapped[bool]
    trend: Mapped[str]

    def __str__(self) -> str:
        return f"VolumeMotion: {self.symbol}, delta: {self.delta}, trend: {self.trend}, price: {self.price}"
