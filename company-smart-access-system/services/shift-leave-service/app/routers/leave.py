from fastapi import APIRouter
from app.database import database
from app.models import leaves

router = APIRouter()

@router.post("/request-leave/")
async def request_leave(data: dict):
    query = leaves.insert().values(
        employee_id=data["employee_id"],
        start_date=data["start_date"],
        end_date=data["end_date"],
        type=data["type"]
    )
    leave_id = await database.execute(query)
    return {"leave_id": leave_id}

@router.get("/pending-leaves/")
async def get_pending():
    query = leaves.select().where(leaves.c.status == "pending")
    return await database.fetch_all(query)
