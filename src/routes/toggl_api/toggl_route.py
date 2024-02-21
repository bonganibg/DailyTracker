from fastapi import APIRouter, HTTPException

from src.services.toggl_tracker_client_service import TogglClient
from src.services.models.toggl_event_model import TogglEvent
from src.services.models.toggl_project_model import TogglProject 
from src.services.models.toggl_workspace_model import TogglWorkspace
from src.services.models.toggl_auth_model import TogglUserAuth


client = TogglClient()

router = APIRouter(
    prefix="/api/v1/toggl",
    tags=["toggl"]
)



@router.get("/auth", status_code=200)
async def auth(user_details: TogglUserAuth) -> dict:
    result = client.login(user_details)

    if (result):
        return {
            "Message": "success",
            "api_token": result
        }
    
    if (result == None):
        raise HTTPException(status_code=500, detail="Internal server error")
    
    if (result == False):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
@router.get('/workspace')
async def get_workspaces(api_token: str) -> list[TogglWorkspace]:
    result = client.get_all_workspaces(api_token)

    if (result):
        return {
            "Message": "success",
            "workspaces": result
        }
    
    if (result == False):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if (result == None):
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get('/project')
async def get_projects(workspace_id: str, api_token: str) -> list[TogglProject]:
    result = client.get_projects(workspace_id, api_token)

    if (result):
        return {
            "Message": "success",
            "projects": result
        }

    if (result == False):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if (result == None):
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/event', status_code=200, response_model=dict)
async def post_event(event: TogglEvent, api_token: str):
    result = client.create_toggl_event(event, api_token)

    if (result):
        return {
            "Message": "success"
        }
    
    if (result == False):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if (result == None):
        raise HTTPException(status_code=500, detail="Internal server error")