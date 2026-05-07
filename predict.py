print("Predict script started...")

import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

clf = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")

model = SentenceTransformer("all-MiniLM-L6-v2")


def predict(text):

    vec = model.encode([text])

    probs = clf.predict_proba(vec)[0]

    for label, p in zip(le.classes_, probs):
        print(f"{label}: {p:.2f}")

    pred = le.inverse_transform([np.argmax(probs)])[0]

    print("\nPrediction:", pred)

    responses = {
        "positive": "I'm glad to hear things are feeling positive right now.",

        "neutral": "Thanks for sharing. Want to tell me a little more about your day?",

        "negative": "That sounds emotionally difficult. I'm glad you're expressing it instead of holding it in.",

        "high risk": "It sounds like you're overwhelmed right now. Reaching out to someone you trust or grounding yourself could help."
    }

    print("\nChatbot Response:")
    print(responses[pred])

    if "okay" in text.lower() or "fine" in text.lower():
        print("Note: soft neutral/positive language detected")


while True:

    text = input("\nEnter how you feel (or type 'quit'): ")

    if text.lower() == "quit":
        break

    predict(text)