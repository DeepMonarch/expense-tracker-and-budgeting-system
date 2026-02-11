import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = "model.pkl"
VECT_PATH = "vectorizer.pkl"

def train_model(data):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data["description"])
    y = data["category"]

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECT_PATH)

def predict_category(text):
    text = text.lower()

    rules = {
        "Food": ["zomato", "swiggy", "restaurant", "coffee", "pizza", "burger", "food"],
        "Travel": ["uber", "ola", "flight", "train", "bus", "fuel", "taxi", "travel", "transport"],
        "Shopping": ["amazon", "flipkart", "myntra", "clothes", "shopping"],
        "Bills": ["electricity", "rent", "wifi", "internet", "water"],
        "Entertainment": ["movie", "netflix", "spotify", "game"]
    }

    for category, keywords in rules.items():
        for word in keywords:
            if word in text:
                return category

    return "Other"

def detect_anomaly(amounts):
    clf = IsolationForest(contamination=0.1)
    preds = clf.fit_predict(amounts.reshape(-1,1))
    return preds
