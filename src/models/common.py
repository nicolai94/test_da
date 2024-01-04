from datetime import datetime

from sqlalchemy import BigInteger, DateTime, func, Integer
from sqlalchemy.orm import Mapped, mapped_column


class MyModelMixin:
    id: Mapped[int] = mapped_column(Integer, index=True, unique=True, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())