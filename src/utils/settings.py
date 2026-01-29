from pydantic_settings import SettingsConfigDict, BaseSettings

class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
    DATABASE_URL : str
    JWT_SECRET: str
    REFRESH_TOKEN_EXPIRY_TIME: int
    ACCESS_TOKEN_EXPIRY_TIME: int
    ALGORITHM: str


settings = Setting()