from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.api_settings import get_api_settings

from api.app.router import todo_router

get_api_settings.cache_clear()
app = FastAPI(**get_api_settings().fastapi_kwargs)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


app.include_router(todo_router.router)
