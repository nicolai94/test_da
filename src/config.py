from pathlib import Path
from typing import Optional, Any

from pydantic import PostgresDsn
from pydantic.v1 import validator
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    ENV: str = "local"
    PROJECT_NAME: str = "test"
    VERSION: str = "0.0.1"
    PREFIX: str = "/api"

    POSTGRES_SERVER: str = "0.0.0.0:5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "app"
    DB_ECHO: bool = False
    SQLALCHEMY_DATABASE_URI: str ="sqlite:///./sql_app.db" # f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    # SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    #
    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def check_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
    #     if isinstance(v, str):
    #         return v
    #     return PostgresDsn.build(
    #         scheme="postgresql",
    #         user=values.get("POSTGRES_USER"),
    #         password=values.get("POSTGRES_PASSWORD"),
    #         host=values.get("POSTGRES_SERVER"),
    #         path=f"/{values.get('POSTGRES_DB') or ''}",
    #     )



settings = Settings()
