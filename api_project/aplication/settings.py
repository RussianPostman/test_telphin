from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    TARIFFS_URL: str = None
    TARIFFS_API_KEY: str = None

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
