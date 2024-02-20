from src.services.supabase_client_service import SupabaseClientService
from src.models.expected_hours_model import ExpectedHour
from src.controllers.expected_hours_controller import ExpectedHoursController

client = SupabaseClientService()
controller = ExpectedHoursController(client)

result = controller.get_expected_hours("a429c6f2-fe27-4499-8258-4555918bdd94")
print(result)