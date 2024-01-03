from sqlalchemy import Column, String

from src.db import Base
from src.models.common import MyModelMixin


class User(MyModelMixin, Base):
    __tablename__ = 'user'

    login: str = Column(String(255), nullable=False)
    password: str = Column(String(255), nullable=False)
