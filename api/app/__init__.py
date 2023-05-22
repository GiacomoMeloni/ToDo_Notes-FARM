import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.api_settings import get_api_settings

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from api.app.config import settings
from api.app.router import health_router
from api.app.router import user_router
from api.app.router import auth_router
from api.common.logger.setup import logger_setup

from api.app.models.user_model import User

logger_setup()
logger = logging.getLogger(__name__)


get_api_settings.cache_clear()
app = FastAPI(title=settings.PROJECT_NAME,
              openapi_url=f"{settings.PREFIX}/openapi.json",
              docs_url=f"{settings.PREFIX}/docs",
              redoc_url=f"{settings.PREFIX}/redoc")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.on_event("startup")
async def app_init():
    """
        initialize application services
    :return:
    """

    db_client: AsyncIOMotorClient = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todo

    await init_beanie(database=db_client,
                      document_models=[User])

app.include_router(todo_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)
