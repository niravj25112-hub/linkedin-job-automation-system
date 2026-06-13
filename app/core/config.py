from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "LinkedIn Job Automation System"
    app_env: str = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    database_url: str = Field(
        default="postgresql+psycopg2://postgres:postgres@localhost:5432/linkedin_jobs"
    )

    jwt_secret_key: str = "change-me-with-a-long-random-secret"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    gmail_client_id: str | None = None
    gmail_client_secret: str | None = None
    gmail_redirect_uri: str | None = None
    gmail_sender_email: str | None = None

    job_search_lookback_hours: int = 24
    job_keywords: str = "Java Developer C2C,Business Analyst C2C,Project Manager C2C,Data Analyst C2C"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def keyword_filters(self) -> list[str]:
        return [keyword.strip() for keyword in self.job_keywords.split(",") if keyword.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

