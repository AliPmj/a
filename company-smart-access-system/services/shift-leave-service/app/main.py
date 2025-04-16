from fastapi import FastAPI
from app.database import database, metadata, engine
from app.routers import shift, leave

metadata.create_all(bind=engine)

app = FastAPI(title="Shift and Leave Service")

app.include_router(shift.router, prefix="/shift", tags=["Shift"])
app.include_router(leave.router, prefix="/leave", tags=["Leave"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
