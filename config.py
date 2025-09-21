#  настройки приложения, такие как параметры подключения к базам данных, ключи API, настройки логирования и другие константы

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[
            ".env",
        ],
        env_file_encoding="utf-8",
    )
    DEBUG: bool = True
    DB_PORT: str
    DB_HOST: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    @property
    def DB_URL(self):
        return f"postgresql+psycopg2://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"


settings = Config()
