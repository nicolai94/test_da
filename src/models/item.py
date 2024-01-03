from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base
from src.models.common import MyModelMixin


class Item(MyModelMixin, Base):
    __tablename__ = 'item'

    name: str = Column(String(255), nullable=False)
    user_id: int = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="items")