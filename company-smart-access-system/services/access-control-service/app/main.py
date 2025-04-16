from fastapi import FastAPI
from app.routes import access

app = FastAPI(title="Access Control Service")

app.include_router(access.router, prefix="/access", tags=["Access Control"])

@app.get("/")
def root():
    return {"message": "Access Control Service is running"}
