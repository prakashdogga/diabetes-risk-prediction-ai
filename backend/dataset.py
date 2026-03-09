# Save this as E:\diabetic_or_not\download_data.py
import os
import pandas as pd
import requests

BASE_DIR = r"E:\diabetic_or_not"
os.makedirs(BASE_DIR, exist_ok=True)

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
df = pd.read_csv(url, header=None)
df.columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
              "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
df.to_csv(os.path.join(BASE_DIR, "diabetes.csv"), index=False)
print("Dataset saved to E:\\diabetic_or_not\\diabetes.csv")
