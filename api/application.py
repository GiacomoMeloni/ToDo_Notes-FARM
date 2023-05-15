import uvicorn

from api.app.config import Settings

settings = Settings()

if __name__ == "__main__":
    uvicorn.run("app:app", host=settings.IP, port=settings.PORT)
