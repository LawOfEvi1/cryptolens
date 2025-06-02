from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.shemas.kline import KlineIn
from db import Kline
from db.database import get_async_session

router = APIRouter(prefix="/kline", tags=["Kline"])

@router.post("/create")
async def create_kline(data: KlineIn, session: AsyncSession = Depends(get_async_session)):
    result = await Kline.create(data.model_dump(), session)
    return {"id": result.id}
