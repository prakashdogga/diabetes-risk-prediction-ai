from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("diabetes_logreg.pkl")
scaler = joblib.load("diabetes_scaler.pkl")

class PatientData(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree: float
    age: float
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running"}
@app.post("/predict")
def predict(data: PatientData):

    features = np.array([[ 
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree,
        data.age
    ]])

    features_scaled = scaler.transform(features)

    prob = float(model.predict_proba(features_scaled)[0][1])

    risk = "Low"
    if prob >= 0.7:
        risk = "High"
    elif prob >= 0.4:
        risk = "Moderate"

    return {"probability": prob, "risk": risk}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)