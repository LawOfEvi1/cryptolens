from sqlalchemy import Boolean, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, MappedColumn

from db.models.BaseORMModel import BaseORMModel


class NotificationSettingsByRank(BaseORMModel):
    __tablename__ = 'notification_settings_by_rank'

    user_id: Mapped[int] = MappedColumn(ForeignKey("users.id"))
    enable_percent_alert: Mapped[bool] = MappedColumn(Boolean, default=True)
    delta_threshold: Mapped[float] = MappedColumn(Float, default=0.02)
    last_price: Mapped[float] = MappedColumn(Float)
    current_rate: Mapped[float] = MappedColumn(Float)
    track_price_change: Mapped[bool] = MappedColumn(Boolean, default=True)

    def __str__(self) -> str:
        return f"NotificationSettings(user_id={self.user_id}, delta_threshold={self.delta_threshold})"
