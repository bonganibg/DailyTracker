from src.services.supabase_client_service import SupabaseClientService
from src.controllers.hours_off_controller import HoursOffController
from src.models.hours_off_model import HoursOff

from datetime import datetime


client = SupabaseClientService()
controller = HoursOffController(client)

result = controller.get_hours_off("a429c6f2-fe27-4499-8258-4555918bdd94","2024-02-1", "2024-02-11")

print(result)