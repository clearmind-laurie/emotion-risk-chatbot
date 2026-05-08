import streamlit as st
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model files
clf = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Page setup
st.set_page_config(page_title="Emotion Classifier", page_icon="🧠")

st.title("🧠 Emotion & Risk Classification Chatbot")

st.caption("Built with Python, NLP, Sentence Transformers, scikit-learn, and Streamlit")

st.sidebar.title("About")

st.sidebar.info(
    "This NLP chatbot uses sentence embeddings and machine learning "
    "to classify emotional tone and contextual relapse-risk language."
)

st.sidebar.write("Built by Laurie Baldwin")

st.info(
    "This app analyzes emotional tone and contextual relapse-risk language using machine learning."
)

Also make sure your input label says:

st.markdown(
    "### Real-time emotional and contextual risk classification powered by NLP"
)

# User input
text = st.text_input("Enter a message to analyze:")

# Chatbot responses
responses = {
    "positive": "I'm glad to hear things are feeling positive right now.",
    "neutral": "Thanks for sharing. Want to tell me a little more about your day?",
    "negative": "That sounds emotionally difficult. I'm glad you're expressing it instead of holding it in.",
    "high risk": "It sounds like you're overwhelmed right now. Reaching out to someone you trust or grounding yourself could help."
}

# Analyze button
if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        vec = model.encode([text])
        probs = clf.predict_proba(vec)[0]

        pred = le.inverse_transform([np.argmax(probs)])[0]
        confidence = max(probs)

        st.subheader("Results")

        for label, p in zip(le.classes_, probs):
            st.write(f"{label}: {p:.2f}")

        st.success(f"Prediction: {pred}")
        st.info(f"Confidence: {confidence:.2f}")

        st.subheader("Chatbot Response")
        st.write(responses[pred])

        if pred == "high risk":
            st.error("⚠️ High-risk language detected")
        elif pred == "negative":
            st.warning("Negative emotional state detected")
        else:
            st.success("No risk detected")
