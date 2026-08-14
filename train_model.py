import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


DATASET = "spam.csv"
MODEL = "model.pkl"


def load_dataset():
    if not os.path.exists(DATASET):
        raise FileNotFoundError(
            "spam.csv was not found. Create/download a CSV with columns: label,message"
        )

    df = pd.read_csv(DATASET)

    required = {"label", "message"}
    if not required.issubset(df.columns):
        raise ValueError("spam.csv must contain 'label' and 'message' columns.")

    df = df.dropna(subset=["label", "message"]).copy()
    df["label"] = df["label"].astype(str).str.lower().map({"ham": 0, "spam": 1})
    df = df.dropna(subset=["label"])

    return df


def main():
    df = load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        df["message"],
        df["label"].astype(int),
        test_size=0.2,
        random_state=42,
        stratify=df["label"]
    )

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
            max_features=30000
        )),
        ("classifier", MultinomialNB())
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    print("\nAI Spam Email Checker - Model Evaluation")
    print("-" * 45)
    print(f"Accuracy : {accuracy_score(y_test, predictions) * 100:.2f}%")
    print(f"Precision: {precision_score(y_test, predictions, zero_division=0) * 100:.2f}%")
    print(f"Recall   : {recall_score(y_test, predictions, zero_division=0) * 100:.2f}%")
    print(f"F1 Score : {f1_score(y_test, predictions, zero_division=0) * 100:.2f}%")

    joblib.dump(pipeline, MODEL)
    print(f"\nModel saved as {MODEL}")


if __name__ == "__main__":
    main()
