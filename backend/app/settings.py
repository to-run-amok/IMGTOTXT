from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HF_TOKEN: str = "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"
    HF_MODEL: str = "microsoft/trocr-base-printed"
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    class Config:
        env_file = ".env"

settings = Settings()