from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.db import Base
from src.models.common import MyModelMixin


class User(MyModelMixin, Base):
    __tablename__ = 'user'

    login: str = Column(String(255), nullable=False)
    password: str = Column(String(255), nullable=False)
    item: Mapped["Item"] = relationship(back_populates="user")

    def __repr__(self):
        return f'{self.login}'


class Item(MyModelMixin, Base):
    __tablename__ = 'item'

    name: str = Column(String(255), nullable=False)
    user_id: int = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="item")

    def __repr__(self):
        return f'{self.name}'