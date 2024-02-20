from src.services.supabase_client_service import SupabaseClientService
from src.controllers.user_controller import UserController

client = SupabaseClientService()
controller = UserController(client)

# result = controller.get_expected_hours("a429c6f2-fe27-4499-8258-4555918bdd94")
result = controller.get_user_details("a429c6f2-fe27-4499-8258-4555918bdd94")
print(result.id)