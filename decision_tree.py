import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

def train():
    with open("characters.json", "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    X = df.drop(columns=["name"])
    y = df["name"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    joblib.dump(model, "model.pkl")
    print("✅ Model trained and saved to model.pkl")

if __name__ == "__main__":
    train()
