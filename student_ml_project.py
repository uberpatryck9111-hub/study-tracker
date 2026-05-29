
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# 1. Load data
df = pd.read_csv("study_data.csv")

# 2. Features and labels
X = df.drop("passed", axis=1)
y = df["passed"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Build pipeline (scaling + model)
model = Pipeline([
    ("scaler", StandardScaler()),
    ("logreg", LogisticRegression())
])

# 5. Train
model.fit(X_train, y_train)

# 6. Predict
predictions = model.predict(X_test)

# 7. Evaluate
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nReport:\n", classification_report(y_test, predictions))

# 8. Predict new student (IMPORTANT FIX)
new_student = pd.DataFrame([[
    6, 8, 90, 5
]], columns=[
    "hours_studied",
    "sleep_hours",
    "attendance",
    "practice_exams"
])

print("New prediction:", model.predict(new_student))