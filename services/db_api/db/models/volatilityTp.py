import datetime
from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, MappedColumn

from db.database import async_session_factory
from db.models.BaseORMModel import BaseORMModel  # базовый класс


class VolatilityTp(BaseORMModel):
    __tablename__ = 'volatility_tp'

    symbol: Mapped[str] = MappedColumn(String, ForeignKey("trading_pair.symbol"), nullable=False)
    price_from: Mapped[float]
    price_current: Mapped[float]
    data_time: Mapped[datetime.datetime]
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger)
    perc_change: Mapped[float]
    up: Mapped[bool]

    def __str__(self) -> str:
        return f"symbol: {self.symbol}, price_current: {self.price_current}"


async def insert_volatility_tp(
    symbol: str,
    timestamp_ms: int,
    current_time: datetime.datetime,
    percChange: float,
    price_current: float,
    price_from: float,
    up: bool,
) -> None:
    try:
        payload = {
            "symbol": symbol,
            "timestamp_ms": timestamp_ms,
            "data_time": current_time,
            "perc_change": percChange,
            "price_current": price_current,
            "price_from": price_from,
            "up": up,
        }

        async with async_session_factory() as session:
            await VolatilityTp.create(payload, session)

    except Exception as e:
        print(f"Ошибка при вставке в volatility_tp: {e}")
