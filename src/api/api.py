from fastapi import APIRouter
from src.api.routers.item import router as item_router

api_router = APIRouter()

api_router.include_router(item_router, prefix="/item", tags=["item"])
