from pydantic_settings import BaseSettings
from pydantic import field_validator
from functools import lru_cache


class Settings(BaseSettings):
    groq_api_key: str
    groq_model: str = "llama-3.3-70b-versatile"
    port: int = 8000
    env: str = "development"

    @classmethod
    @field_validator("*", mode="before")
    def strip_whitespace(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()