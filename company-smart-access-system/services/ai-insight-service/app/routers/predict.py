from fastapi import APIRouter, Body
from app.ai_engine import detect_anomalies, predict_absence

router = APIRouter()

@router.post("/anomaly/attendance")
def anomaly_attendance(data: list[dict] = Body(...)):
    return detect_anomalies(data)

@router.post("/predict/absence")
def predict_absence_api(features: dict = Body(...)):
    return predict_absence(features)
