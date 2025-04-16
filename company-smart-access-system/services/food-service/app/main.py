from fastapi import FastAPI
from app.routes import food

app = FastAPI(title="Food Automation Service")

app.include_router(food.router, prefix="/food", tags=["Food Service"])

@app.get("/")
def root():
    return {"message": "Food Service is running"}
