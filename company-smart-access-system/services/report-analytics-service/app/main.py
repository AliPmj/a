from fastapi import FastAPI
from app.database import database
from app.routers import report

app = FastAPI(title="Report & Analytics Service")

app.include_router(report.router, prefix="/report", tags=["Reports"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
