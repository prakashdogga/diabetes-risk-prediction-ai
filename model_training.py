# backend/model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model():
    # Load dataset (adapt path/columns to your CSV)
    df = pd.read_csv("diabetes.csv")  # e.g. Pima dataset [web:8]

    features = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
    ]
    X = df[features]
    y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    print("Train accuracy:", model.score(X_train, y_train))
    print("Test accuracy:", model.score(X_test, y_test))

    joblib.dump(model, "diabetes_logreg.pkl")
    joblib.dump(scaler, "diabetes_scaler.pkl")

if __name__ == "__main__":
    train_and_save_model()
