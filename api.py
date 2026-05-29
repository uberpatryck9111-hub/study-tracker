
from fastapi import FastAPI
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Training data
df = pd.read_csv("study_data.csv")

X = df.drop("passed", axis=1)
y = df["passed"]

# Build model
model = Pipeline([
    ("scaler", StandardScaler()),
    ("logreg", LogisticRegression())
])

# Train model
model.fit(X, y)

# Create API
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student ML API is running"}

@app.post("/predict")
def predict(
    hours_studied: float,
    sleep_hours: float,
    attendance: float,
    practice_exams: float
):
    student = pd.DataFrame([[
        hours_studied,
        sleep_hours,
        attendance,
        practice_exams
    ]], columns=[
        "hours_studied",
        "sleep_hours",
        "attendance",
        "practice_exams"
    ])

    prediction = model.predict(student)[0]

    return {
        "prediction": int(prediction)
    }

