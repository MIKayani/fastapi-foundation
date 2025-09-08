from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application details
    APP_TITLE: str = "FastApi_Foundation"
    APP_VERSION: str = "Beta_1.0.0"
    APP_DESCRIPTION: str = "APIs for the FastApi_Foundation"

    # CORS
    CORS_ALLOWED_ORIGINS: str = "*"
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOWED_METHODS: str = "*"
    CORS_ALLOWED_HEADERS: str = "*"

    # Docs Auth
    DOCS_USERNAME: str = "admin"
    DOCS_PASSWORD: str = "admin"

    # Database
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DATABASE_INIT: bool = False

    # Logging
    LOGLEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'ignore'