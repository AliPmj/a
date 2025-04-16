from fastapi import FastAPI
from app.database import database
from app.routers import predict

app = FastAPI(title="AI & Insights Service")

app.include_router(predict.router, prefix="/ai", tags=["AI Services"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
