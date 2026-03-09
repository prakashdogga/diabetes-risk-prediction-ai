# 🩺 Diabetes Risk Prediction AI

An AI-powered web application that predicts whether a person is at risk of diabetes using Machine Learning.
The model analyzes health-related inputs and provides an instant prediction through a simple web interface.

---

## 🚀 Features

* Machine Learning model for diabetes risk prediction
* Fast API backend for model inference
* Interactive frontend for user input
* Real-time prediction results
* Clean and simple UI

---

## 🧠 Machine Learning Model

The model is trained using medical diagnostic data to predict whether a patient is likely to have diabetes.

Typical input features include:

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

The trained model processes these inputs and predicts whether the person is **Diabetic or Not Diabetic**.

---

## 🛠️ Tech Stack

**Machine Learning**

* Python
* Scikit-learn
* Pandas
* NumPy

**Backend**

* FastAPI

**Frontend**

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```
diabetes-risk-prediction-ai
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── static
    └── script.js
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/diabetes-risk-prediction-ai.git
```

Move into the project folder:

```
cd diabetes-risk-prediction-ai
```

Create virtual environment:

```
python -m venv venu
```

Activate environment:

**Windows**

```
venu\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```
uvicorn app:app --reload
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

Enter the health parameters and get the prediction instantly.

---

## 📊 Example Prediction

Input health data →
Machine learning model processes features →
Output:

```
Prediction: Diabetic
```

or

```
Prediction: Not Diabetic
```

---

## 📌 Future Improvements

* Deploy the application to cloud
* Improve model accuracy
* Add better UI design
* Add authentication system
* Build a full medical dashboard

---

## 👨‍💻 Author

**Prakash**

Machine Learning Enthusiast
Passionate about building AI-powered solutions.

GitHub:
https://github.com/prakashdogga

LinkedIn:
https://www.linkedin.com/in/prakash-30b350356
