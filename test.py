from src.services.supabase_client_service import SupabaseClientService
from src.controllers.hours_worked_controller import HoursWorkedController
from src.models.hours_worked_model import HoursWorked


import random


client = SupabaseClientService()
controller = HoursWorkedController(client)

result = controller.get_hours_worked("a429c6f2-fe27-4499-8258-4555918bdd94", "2024-01-01", "2024-01-30")
print(result)
