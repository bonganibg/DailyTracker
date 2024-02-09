from fastapi import APIRouter
from src.routes import user_route


# Add the routers 
router = APIRouter()
router.include_router(user_route.router)