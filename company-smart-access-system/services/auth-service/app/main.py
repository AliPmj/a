from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import httpx
from jose import jwt, JWTError
from typing import List
from datetime import datetime, timedelta

# مسیر احراز هویت و تنظیمات JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://auth-service:8005/login")

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

app = FastAPI(title="Smart Campus Gateway")

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# بررسی نقش کاربر
def check_role(token: str, role: str):
    payload = verify_token(token)
    if payload.get("role") != role:
        raise HTTPException(status_code=403, detail="Not authorized")
    return payload

@app.post("/attendance/checkin")
async def checkin(request: Request, token: str = Depends(oauth2_scheme)):
    check_role(token, "employee")
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post("http://attendance-service:8001/checkin", json=body)
    return response.json()

# بقیه مسیرها هم به همین شکل
