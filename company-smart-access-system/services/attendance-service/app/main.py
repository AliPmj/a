from fastapi import FastAPI
from app.routes import attendance

app = FastAPI(title="Attendance Service")

app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])

@app.get("/")
def root():
    return {"message": "Attendance Service is running"}
