import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("characters.csv")

# Convert categorical data to numerical
X = df.drop(columns=["name"])
X = X.applymap(lambda x: 1 if x == "Yes" else 0)
y = df["name"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

def predict_character(answers):
    """Predicts character based on Yes/No answers"""
    input_data = [1 if ans == "Yes" else 0 for ans in answers]
    return model.predict([input_data])[0]
