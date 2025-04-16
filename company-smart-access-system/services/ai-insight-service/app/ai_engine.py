import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LogisticRegression
import joblib

# مدل ساده برای تشخیص ناهنجاری در تردد
def detect_anomalies(data: list[dict]):
    df = pd.DataFrame(data)
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df.select_dtypes(include=[np.number]))
    return df[df['anomaly'] == -1].to_dict(orient='records')

# مدل ساده برای پیش‌بینی غیبت کارمند
def predict_absence(features: dict):
    model = joblib.load("app/models/absence_model.joblib")
    X = pd.DataFrame([features])
    proba = model.predict_proba(X)[0][1]
    return {"probability_of_absence": round(proba, 2)}
