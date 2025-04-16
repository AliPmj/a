from fastapi import APIRouter, Request
import httpx

router = APIRouter()
ATTENDANCE_URL = "http://attendance-service:8001"

@router.post("/checkin")
async def checkin(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ATTENDANCE_URL}/checkin", json=body)
    return response.json()
