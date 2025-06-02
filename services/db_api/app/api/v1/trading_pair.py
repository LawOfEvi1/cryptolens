from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.shemas.kline import KlineIn
from app.shemas.trading_pair import TradingPairIn
from db import Kline, TradingPair
from db.database import get_async_session

router = APIRouter(prefix="/trading-pair", tags=["trading-pair"])

@router.post("/create")
async def create_trading_pair(data: TradingPairIn, session: AsyncSession = Depends(get_async_session)):
    result = await TradingPair.create(data.model_dump(), session)
    return {"trading pair - ": result.symbol}
