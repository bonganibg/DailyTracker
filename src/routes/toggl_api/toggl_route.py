from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError

from src.services.toggl_tracker_client_service import TogglClient
from src.services.models.toggl_event_model import TogglEvent
from src.services.models.toggl_project_model import TogglProject 
from src.services.models.toggl_workspace_model import TogglWorkspace
from src.services.models.toggl_auth_model import TogglUserAuth
from datetime import timedelta


client = TogglClient()

router = APIRouter(
    prefix="/api/v1/toggl",
    tags=["toggl"]
)

def generate_token(user_id: str):
    expires_delta = timedelta(minutes=60)
    expires = datetime.utcnow() + expires_delta

    encode = {"sub": user_id, "exp": expires}

    return jwt.encode(encode, "secret", algorithm="HS256")


async def validate_user_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/toggl/login"))):
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        user_id: str = payload.get("sub")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")



@router.post("/login", status_code=200)
async def login(user_details: OAuth2PasswordRequestForm = Depends()):
    user = TogglUserAuth(email=user_details.username, 
                         password=user_details.password)
    
    result = client.login(user)

    token = generate_token(result)

    if (result):
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    
    if (result == None):
        raise HTTPException(status_code=500, detail="Internal server error")
    
    if (result == False):
        raise HTTPException(status_code=400, detail="Invalid credentials")


@router.get("/auth", status_code=200)
async def auth(user_details: TogglUserAuth) -> dict:
    result = client.login(user_details)
    print(result)

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