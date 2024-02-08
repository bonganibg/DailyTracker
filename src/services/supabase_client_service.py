from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

class SupabaseClientService():
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def fetch_one(self, table_name: str, id: int):
        return self.supabase.table(table_name).select("*").eq('id', id).execute()

    def fetch_all(self, table_name: str, user_id: str):
        return self.supabase.table(table_name).select("*").eq("user_id", user_id).execute()
    
    def insert(self, table_name: str, data: dict):
        return self.supabase.table(table_name).insert(data).execute()
    
    def update(self, table_name: str, data: dict, id: int):
        return self.supabase.table(table_name).update(data).eq('id', id).execute()
    
    def delete(self, table_name: str, id: int):
        return self.supabase.table(table_name).delete().eq('id', id).execute()
    
    def get_in_date_range(self, table_name: str, user_id: str, start_date: str, end_date: str):
        return self.supabase.table(table_name).select("*").eq('user_id', user_id).gte('date', start_date).lte('date', end_date).execute()

    
    def clear_records(self, table_name: str, user_id: str):
        return self.supabase.table(table_name).delete().eq('user_id', user_id).execute()
        

    