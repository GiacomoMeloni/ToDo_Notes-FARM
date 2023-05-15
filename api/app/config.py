import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    IP = os.environ.get('HOST_URL', '127.0.0.1')
    PORT = os.environ.get('HOST_PORT', 5000)


settings = Settings()
