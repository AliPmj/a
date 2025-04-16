from fastapi import APIRouter
from app.database import database
from app.models import shifts
from datetime import date, time

router = APIRouter()

@router.post("/assign-shift/")
async def assign_shift(data: dict):
    query = shifts.insert().values(
        employee_id=data["employee_id"],
        date=data["date"],
        start_time=data["start_time"],
        end_time=data["end_time"],
        remote=data.get("remote", False)
    )
    shift_id = await database.execute(query)
    return {"shift_id": shift_id}
