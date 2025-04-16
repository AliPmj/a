from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class AccessRequest(BaseModel):
    user_id: int
    location: str
    access_time: datetime

@router.post("/check")
def check_access(data: AccessRequest):
    return {
        "status": "granted",
        "user_id": data.user_id,
        "location": data.location,
        "time": str(data.access_time)
    }
