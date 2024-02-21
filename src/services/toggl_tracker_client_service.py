import requests
import json

from requests.models import Response


from src.services.models.toggl_event_model import TogglEvent
from src.services.models.toggl_workspace_model import TogglWorkspace
from src.services.models.toggl_project_model import TogglProject

class TogglService:

    def login(self, email: str, password: str):
        try:
            response = requests.get("https://api.track.toggl.com/api/v9/me", auth=(email, password), timeout=10)
        except Exception as e:
            print(e)
            return None
        
        if (self.__is_successful(response)):
            api_token = response.json()["api_token"]
            return api_token
        
        return False
    
    def get_all_workspaces(self, api_token: str):

        response = self.__get_request("https://api.track.toggl.com/api/v9/workspace", api_token)

        if (response == None):
            return None
        
        if (not self.__is_successful(response)):
            return None
        
        results = response.json()

        workspaces = [TogglWorkspace(**result) for result in results]

        return workspaces 
    
    def get_projects(self, workspace_id: str, api_token: str):
        url = f"https://api.track.toggl.com/api/v9/workspace/{workspace_id}/projects"
        response = self.__get_request(url, api_token)

        if (response == None):
            return None
        
        if (not self.__is_successful(response)):
            return None
        
        response = response.json()

        return [TogglProject(**result) for result in response]
    
    def create_toggl_event(self, event: TogglEvent, wid: int,  api_token: str):
        url = f"https://api.track.toggl.com/api/v9/workspaces/{wid}/time_entries"

        data = json.dumps(event.model_dump())

        try:
            response = requests.post(url, data=data, auth=(api_token, "api_token"), timeout=10)
        except Exception as e:
            print(e)
            return None
        
        if (not self.__is_successful(response)):
            print(response.text)
            return False
        
        return True

    def __get_request(self, url: str, api_token: str):
        try:
            response = requests.get(url, auth=(api_token, "api_token"), timeout=10)
            return response
        except Exception as e:
            print(e)
            return None

    def __is_successful(self, response: Response) -> bool:
        return True if 100 < response.status_code < 300 else False