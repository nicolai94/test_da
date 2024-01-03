from typing import Generator
from src.db import SessionLocal
from src.logger import get_logger


logger = get_logger("deps")


def get_db() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
