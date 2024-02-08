from src.models.expected_hours_model import ExpectedHour
from src.services.database_service_interface import DatabaseServiceInterface

class ExpectedHoursController():
    TABLE_NAME = "expected_hours"


    def __init__(self, database_service: DatabaseServiceInterface) -> None:
        self.__database_service = database_service
        

    def update_expceted_hours(self, expceted_hours_dict: list[ExpectedHour], user_id: str):
        self.__database_service.clear_records(self.TABLE_NAME, user_id)

        for expected_hour in expceted_hours_dict:
            self.__database_service.insert(self.TABLE_NAME, expected_hour.model_dump())
        
    

'''
Gets the expected working hours in the form of a JSON object,
We need to deconstruct this object so that we can work with it in our code.
'''