from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# مدل ثبت حضور
class AttendanceRecord(BaseModel):
    user_id: int
    check_type: str  # ورود یا خروج
    timestamp: datetime

@router.post("/check")
def check_in_out(record: AttendanceRecord):
    return {
        "status": "success",
        "data": record
    }

@router.get("/status/{user_id}")
def get_attendance_status(user_id: int):
    return {
        "user_id": user_id,
        "status": "present",
        "last_check": str(datetime.now())
    }
