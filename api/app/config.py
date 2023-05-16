import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    IP: str = os.environ.get('HOST_URL', '127.0.0.1')
    PORT: int = os.environ.get('HOST_PORT', 5000)
    ROOT_API_PATH: str = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
    RESOURCE_PATH: str = os.path.join(ROOT_API_PATH, 'resources')


settings = Settings()
