from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt
import httpx
from fastapi import FastAPI
from app.routes import attendance, food, access, ai

app = FastAPI(title="Smart Campus Gateway")

# ثبت مسیرهای هر سرویس
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(food.router, prefix="/food", tags=["Food"])
app.include_router(access.router, prefix="/access", tags=["Access Control"])
app.include_router(ai.router, prefix="/ai", tags=["AI & Insights"])

app = FastAPI(title="Gateway Service")

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

services_map = {
    "/presence": "http://presence-service:8001",
    "/food": "http://food-service:8002",
    "/access": "http://access-service:8003",
    "/auth": "http://auth-service:8004"
}

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        return None

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(full_path: str, request: Request):
    path = "/" + full_path
    prefix = "/" + path.split("/")[1]

    if prefix not in services_map:
        raise HTTPException(status_code=404, detail="Service not found")

    # JWT token check except for /auth
    if not path.startswith("/auth"):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid token")
        token = auth_header.split(" ")[1]
        user = verify_jwt_token(token)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")

    body = await request.body()
    headers = dict(request.headers)
    target_url = services_map[prefix] + path

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body
        )

    return JSONResponse(status_code=response.status_code, content=response.json())
