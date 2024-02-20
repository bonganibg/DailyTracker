import os 
from dotenv import load_dotenv

from fastapi import APIRouter

from src.services.supabase_client_service import SupabaseClientService
from src.controllers.user_controller import UserController
from src.models.user_model import User

load_dotenv()

# Set up dependencies 
client = SupabaseClientService()
user_controller = UserController(client)

router = APIRouter(
    prefix="/api/v1/user",
    tags=["user"]
)

@router.get("/", status_code=200)
def get_users(user_id: str) -> User:
    user_controller.get_user_details(user_id)

@router.put("/", status_code=200)
def update_user(user: User) -> User:
    return user_controller.update_user_details(user)
   