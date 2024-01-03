from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class MyModelMixin:
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())