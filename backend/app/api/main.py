from fastapi import APIRouter

from api.routes import info

# import routes from other modules

api_router = APIRouter()

# .include_router for all modules
api_router.include_router(info.router)