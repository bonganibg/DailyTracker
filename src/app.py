from fastapi import APIRouter
from src.routes import user_route, expected_hours_route


# Add the routers 
router = APIRouter()
router.include_router(user_route.router)
router.include_router(expected_hours_route.router)
