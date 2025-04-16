from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.utils.jwt_handler import create_access_token

router = APIRouter()

fake_users = {
    "admin": {
        "username": "admin",
        "password": "1234",  # فقط برای تست، در عمل رمز هش‌شده می‌مونه
        "role": "admin"
    }
}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    user = fake_users.get(data.username)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
