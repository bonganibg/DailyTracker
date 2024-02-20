from src.services.supabase_client_service import SupabaseClientService
from src.models.hours_off_model import HoursOff

class HoursOffController():
    TABLE_NAME = 'hours_off'

    def __init__(self, database_service: SupabaseClientService) -> None:
        self.__database_service = database_service

    def log_off_hours(self, hours_off: HoursOff):
        self.__database_service.insert(self.TABLE_NAME, hours_off.model_dump())

    def bulk_log_off_hours(self, hours_off_list: list[HoursOff]):
        for hours_off in hours_off_list:
            self.__database_service.insert(self.TABLE_NAME, hours_off.model_dump())

    def get_hours_off(self, user_id: str, start_date: str, end_date: str):
        res = self.__database_service.get_in_date_range(self.TABLE_NAME, user_id, start_date, end_date).data
        return [HoursOff(**hour) for hour in res]

    
