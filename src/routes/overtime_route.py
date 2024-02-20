from dotenv import load_dotenv

from fastapi import APIRouter

from src.services.supabase_client_service import SupabaseClientService
from src.controllers.overtime_controller import OvertimeController
from src.models.overtime_model import Overtime

load_dotenv()

# Setup dependencies
client = SupabaseClientService()
controller = OvertimeController(client)

router = APIRouter(
    prefix="/api/v1/overtime",
    tags=["Overtime"]
)

@router.get("/", status_code=200)
async def get_overtime(user_id: str, start_date: str, end_date: str) -> list[Overtime]:
    return controller.get_overtime(user_id, start_date, end_date)

@router.post("/", status_code=200)
async def log_overtime(overtime: Overtime):
    controller.log_overtime(overtime)

@router.post("/bulk", status_code=200)
async def log_overtime_bulk(overtime: list[Overtime]):
    controller.bulk_log_overtime(overtime)