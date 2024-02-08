import datetime
from services.supabase_client_service import SupabaseClientService
from models.hours_worked_model import HoursWorked

class HoursWorkedController():
    TABLE_NAME = 'hours_worked'

    def __init__(self, database_service: SupabaseClientService) -> None:
        self.__database_service = database_service

    def log_hours_worked(self, hours_worked: HoursWorked) -> None:
        self.__database_service.insert(self.TABLE_NAME, hours_worked.model_dump())

    def bulk_log_hours_worked(self, hours_worked_list: list[HoursWorked]) -> None:
        for hours_worked in hours_worked_list:
            self.__database_service.insert(self.TABLE_NAME, hours_worked.model_dump())

    def get_hours_worked(self, user_id: str, start_date: datetime, end_date: datetime) -> list[HoursWorked]:
        response = self.__database_service.get_in_date_range(self.TABLE_NAME, user_id, start_date, end_date)

        hours_worked = [HoursWorked(**hour) for hour in response]
        return hours_worked