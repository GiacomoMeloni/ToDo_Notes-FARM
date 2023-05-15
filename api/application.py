import uvicorn

from api.app.config import settings

if __name__ == "__main__":
    uvicorn.run("app:app", host=settings.IP, port=settings.PORT)
