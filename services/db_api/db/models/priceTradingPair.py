import datetime
from typing import Optional

from sqlalchemy import Integer, Float, String, ForeignKey, BigInteger
from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy.future import select

from db.database import async_session_factory
from db.models.BaseORMModel import BaseORMModel


class PriceTradingPair(BaseORMModel):
    __tablename__ = 'price_trading_pair'

    symbol: Mapped[str] = MappedColumn(String, ForeignKey("trading_pair.symbol"), nullable=False)

    price: Mapped[float] = MappedColumn(Float, nullable=False)
    data_time: Mapped[datetime.datetime] = MappedColumn(nullable=False)
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger, nullable=False)
    bid1Price: Mapped[float] = MappedColumn(Float, nullable=False)
    bid1Size: Mapped[float] = MappedColumn(Float, nullable=False)
    ask1Price: Mapped[float] = MappedColumn(Float, nullable=False)
    ask1Size: Mapped[float] = MappedColumn(Float, nullable=False)
    lastPrice: Mapped[float] = MappedColumn(Float, nullable=False)
    prevPrice24h: Mapped[float] = MappedColumn(Float, nullable=False)
    price24hPcnt: Mapped[float] = MappedColumn(Float, nullable=False)
    lowPrice24h: Mapped[float] = MappedColumn(Float, nullable=False)
    turnover24h: Mapped[float] = MappedColumn(Float, nullable=False)
    volume24h: Mapped[float] = MappedColumn(Float, nullable=False)
    usdIndexPrice: Mapped[Optional[float]] = MappedColumn(Float, nullable=True)

    def __str__(self) -> str:
        return f"symbol: {self.symbol}, price: {self.price}"

    @classmethod
    async def create_from_params(cls, params: dict, data_time: datetime.datetime, timestamp_ms: int, session):
        # Формируем словарь с полями, которые есть в модели
        payload = {
            "symbol": params["symbol"],
            "price": float(params["lastPrice"]),
            "data_time": data_time,
            "timestamp_ms": timestamp_ms,
            "bid1Price": float(params["bid1Price"]),
            "bid1Size": float(params["bid1Size"]),
            "ask1Price": float(params["ask1Price"]),
            "ask1Size": float(params["ask1Size"]),
            "lastPrice": float(params["lastPrice"]),
            "prevPrice24h": float(params["prevPrice24h"]),
            "price24hPcnt": float(params["price24hPcnt"]),
            "lowPrice24h": float(params["lowPrice24h"]),
            "turnover24h": float(params["turnover24h"]),
            "volume24h": float(params["volume24h"]),
            "usdIndexPrice": float(params.get("usdIndexPrice")) if "usdIndexPrice" in params else None,
        }
        return await cls.create(payload, session)

    @staticmethod
    async def get_price_trading_pair(symbol: str):
        async with async_session_factory() as session:
            result = await session.execute(
                select(PriceTradingPair.price, PriceTradingPair.timestamp_ms)
                .filter(PriceTradingPair.symbol == symbol)
                .order_by(PriceTradingPair.timestamp_ms)
            )
            rows = result.all()
        import pandas as pd
        return pd.DataFrame(rows, columns=["price", "timestamp_ms"])

    @staticmethod
    async def get_last_price_trading_pair(symbol: str) -> Optional[float]:
        async with async_session_factory() as session:
            result = await session.execute(
                select(PriceTradingPair.price)
                .filter(PriceTradingPair.symbol == symbol)
                .order_by(PriceTradingPair.timestamp_ms.desc())
                .limit(1)
            )
            row = result.scalar_one_or_none()
        return row
