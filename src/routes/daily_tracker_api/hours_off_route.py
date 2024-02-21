from dotenv import load_dotenv

from fastapi import APIRouter

from src.services.supabase_client_service import SupabaseClientService
from src.controllers.hours_off_controller import HoursOffController
from src.models.hours_off_model import HoursOff

load_dotenv()

# Setup dependencies
client = SupabaseClientService()
controller = HoursOffController(client)

router = APIRouter(
    prefix="/api/v1/hours_off",
    tags=["Hours Off"]
)

@router.get("/", status_code=200)
async def get_hours_off(user_id: str, start_date: str, end_date: str) -> list[HoursOff]:
    return controller.get_hours_off(user_id, start_date, end_date)

@router.post("/", status_code=200)
async def log_hours_off(hours_off: HoursOff):
    controller.log_off_hours(hours_off)

@router.post("/bulk", status_code=200)
async def log_hours_off_bulk(hours_off: list[HoursOff]):
    controller.bulk_log_off_hours(hours_off)
