from dotenv import load_dotenv

from fastapi import APIRouter

from src.services.supabase_client_service import SupabaseClientService
from src.controllers.expected_hours_controller import ExpectedHoursController
from src.models.expected_hours_model import ExpectedHour

load_dotenv()

# Setup dependencies 
client = SupabaseClientService()
expected_hours_controller = ExpectedHoursController(client)

router = APIRouter(
    prefix="/api/v1/expected_hours",
    tags=["expected_hours"]
)

@router.get("/", status_code=200)
async def get_expected_hours(user_id: str) -> list[ExpectedHour]:
    return expected_hours_controller.get_expected_hours(user_id)

@router.put("/", status_code=200)
async def update_expected_hours(expected_hours: list[ExpectedHour], user_id: str) -> list[ExpectedHour]:
    expected_hours_controller.update_expceted_hours(expected_hours, user_id)

    return {
        "Message": "Updated"
    }