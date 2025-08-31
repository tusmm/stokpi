from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.main import api_router

import os
from dotenv import load_dotenv

TITLE = "TITLE"

app = FastAPI(
    title=TITLE
)

load_dotenv()
APP_ORIGIN = os.getenv('app_origin')
origins = [
    APP_ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)