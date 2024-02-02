from pydantic import AnyUrl, BaseModel, IPvAnyAddress, RedisDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine.url import make_url


class SwaggerSettings(BaseModel):
    APP_VERSION: str = "0.1.0"
    APP_TITLE: str = "Integration-Ais-Ado"
    APP_DESCRIPTION: str = "Сервис для получения информации о местоположении ТС"


class DBSetting(BaseModel):
    # DB settings
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    SQL_ECHO: bool = False

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class RedisSettings(BaseModel):
    # Redis
    REDIS_ENABLED: bool = True
    REDIS_URL: RedisDsn
    REDIS_MAX_POOL_CONNECTION: int = 5
    REDIS_MESSAGES_KEY_PREFIX: str = "tracking:state:device_id"


class Settings(SwaggerSettings, DBSetting, RedisSettings, BaseSettings):
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    ROOT_PATH: str = ""
    API_PREFIX: str = "/api"

    # Auth
    # BEARER_TOKEN: str

    # Server
    HOST: IPvAnyAddress | AnyUrl = "0.0.0.0"  # type: ignore
    PORT: int = 8000
    WORKERS: int | None = None

    model_config = SettingsConfigDict(
        env_file=".environment", 
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
