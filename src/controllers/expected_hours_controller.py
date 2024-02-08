from src.models.expected_hours_model import ExpectedHour
from src.services.supabase_client_service import SupabaseClientService

class ExpectedHoursController():
    TABLE_NAME = "expected_hours"


    def __init__(self, database_service: SupabaseClientService) -> None:
        self.__database_service = database_service
        

    def update_expceted_hours(self, expceted_hours_dict: list[ExpectedHour], user_id: str):
        self.__database_service.clear_records(self.TABLE_NAME, user_id)

        for expected_hour in expceted_hours_dict:
            self.__database_service.insert(self.TABLE_NAME, expected_hour.model_dump())

    def get_expected_hours(self, user_id: str) -> list[ExpectedHour]:
        expected_hours = self.__database_service.fetch_all(self.TABLE_NAME)

        return [ExpectedHour(**expected_hour) for expected_hour in expected_hours]