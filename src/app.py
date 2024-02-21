from fastapi import APIRouter
from src.routes.daily_tracker_api import user_route, expected_hours_route, hours_worked_route, hours_off_route, overtime_route
from src.routes.toggl_api import toggl_route

# Add the routers 
router = APIRouter()
router.include_router(user_route.router)
router.include_router(expected_hours_route.router)
router.include_router(hours_worked_route.router)
router.include_router(hours_off_route.router)
router.include_router(overtime_route.router)

# Toggl
router.include_router(toggl_route.router)