from abc import ABC, abstractstaticmethod

class DatabaseServiceInterface(ABC):
    
    @abstractstaticmethod
    def fetch_one(self, table_name: str, id: int):
        pass

    @abstractstaticmethod
    def fetch_all(self, table_name: str, user_id: str):
        pass

    @abstractstaticmethod
    def insert(self, table_name: str, data: dict):
        pass

    @abstractstaticmethod
    def update(self, table_name: str, id: int, data: dict):
        pass

    @abstractstaticmethod
    def delete(self, table_name: str, id: int):
        pass

    @abstractstaticmethod
    def clear_records(self, table_name: str, user_id: str):
        pass