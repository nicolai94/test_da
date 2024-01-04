from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    ENV: str = "local"
    PROJECT_NAME: str = "test"
    VERSION: str = "0.0.1"
    PREFIX: str = "/api"
    SECRET_KEY: str = "test"
    DB_ECHO: bool = False

    SQLALCHEMY_DATABASE_URI: str ="sqlite:///./sql_app.db"


settings = Settings()
