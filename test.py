from src.services.supabase_client_service import SupabaseClientService
from src.controllers.overtime_controller import OvertimeController
from src.models.overtime_model import Overtime


import random


client = SupabaseClientService()
controller = OvertimeController(client)

result = controller.get_overtime("a429c6f2-fe27-4499-8258-4555918bdd94", "2024-02-01", "2024-02-11")
print(result)