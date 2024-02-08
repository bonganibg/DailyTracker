from models.user_model import User
from services.supabase_client_service import SupabaseClientService

class UserController():
    TABLE_NAME = 'user_details'

    def __init__(self, database_service: SupabaseClientService) -> None:
        self.__database_service = database_service

    def update_user_details(self, user: User) -> None:
        user_details = user.model_dump()
        user_id = user_details.pop('id')
        self.__database_service.update(self.TABLE_NAME, user_details, user_id)

    def get_user_details(self, user_id: str) -> User:
        res = self.__database_service.fetch_one(self.TABLE_NAME, user_id)
        return User(**res)