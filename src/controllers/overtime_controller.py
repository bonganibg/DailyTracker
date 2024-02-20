from src.models.overtime_model import Overtime
from src.services.supabase_client_service import SupabaseClientService

class OvertimeController():
    TABLE_NAME = 'overtime'

    def __init__(self, database_service: SupabaseClientService) -> None:
        self.__database_service = database_service

    def log_overtime(self, overtime: Overtime):
        self.__database_service.insert(self.TABLE_NAME, overtime.model_dump())

    def bulk_log_overtime(self, overtime_list: list[Overtime]):
        for overtime in overtime_list:
            self.__database_service.insert(self.TABLE_NAME, overtime.model_dump())

    def get_overtime(self, user_id: str, start_date: str, end_date: str):
        res = self.__database_service.get_in_date_range(self.TABLE_NAME, user_id, start_date, end_date).data
        return [Overtime(**overtime) for overtime in res]