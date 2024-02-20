from dotenv import load_dotenv

from fastapi import APIRouter

from src.services.supabase_client_service import SupabaseClientService
from src.controllers.hours_worked_controller import HoursWorkedController
from src.models.hours_worked_model import HoursWorked

load_dotenv()

# Setup dependencies
client = SupabaseClientService()
controller = HoursWorkedController(client)

router = APIRouter(
    prefix="/api/v1/hours_worked",
    tags=["Hours Worked"]
)

@router.get("/", status_code=200)
async def get_hours_worked(user_id: str, start_date: str, end_date: str) -> list[HoursWorked]:
    return controller.get_hours_worked(user_id, start_date, end_date)

@router.post("/bulk", status_code=200)
async def bulk_log_hours_worked(hours_worked: list[HoursWorked]):
    controller.bulk_log_hours_worked(hours_worked)

@router.post("/", status_code=200)
async def log_hours_worked(hours_worked: HoursWorked):
    print(hours_worked)
    controller.log_hours_worked(hours_worked)
    