from pydantic_settings import BaseSettings
from functools import lru_cache
import typing as t
from .components import logging_settings


class Settings(BaseSettings):
    logging: t.Dict[str, t.Any] = logging_settings

    db_engine: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
