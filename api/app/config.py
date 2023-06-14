import os
from typing import List
from decouple import Config, RepositoryEnv
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PREFIX: str = '/api/todo/v1'
    IP: str = os.environ.get('HOST_URL', '127.0.0.1')
    PORT: int = os.environ.get('HOST_PORT', 5000)
    ROOT_API_PATH: str = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
    RESOURCE_PATH: str = os.path.join(ROOT_API_PATH, 'resources')
    DOTENV_FILE_PATH: str = os.path.join(RESOURCE_PATH, '.env')
    env_config: Config = Config(RepositoryEnv(DOTENV_FILE_PATH))

    JWT_SECRET_KEY: str = env_config('JWT_SECRET_KEY', cast=str)
    JWT_REFRESH_SECRET_KEY: str = env_config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "DuNNoWToDo"

    MONGO_CONNECTION_STRING: str = env_config("MONGO_CONNECTION_STRING", cast=str)

    class Config:
        case_sensitive: bool = True


settings = Settings()
