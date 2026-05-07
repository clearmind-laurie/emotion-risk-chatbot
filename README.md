\# 🧠 Emotion \& Risk Classification Chatbot



A context-aware NLP chatbot that analyzes emotional tone and relapse-risk language using sentence embeddings and machine learning.



Built with Python, Streamlit, scikit-learn, and Sentence Transformers.



\---



\# 🚀 Project Overview



This application classifies user text into emotional and contextual risk categories:



\- Positive

\- Neutral

\- Negative

\- High Risk



The system uses sentence embeddings and a trained machine learning classifier to detect emotional patterns, contextual distress, and relapse-risk language.



After classification, the chatbot generates supportive conversational responses in real time.



\---



\# 🧩 Features



✅ Real-time emotional classification  

✅ Context-aware relapse-risk detection  

✅ Sentence embeddings using MiniLM  

✅ Interactive Streamlit web interface  

✅ Probability confidence scoring  

✅ Conversational chatbot responses  

✅ Custom-trained dataset  

✅ NLP + Machine Learning pipeline  



\---



\# 🛠 Technologies Used



\- Python

\- Streamlit

\- scikit-learn

\- Sentence Transformers

\- NumPy

\- Joblib



\---



\# 🧠 Machine Learning Workflow



The project follows a full NLP pipeline:



```text

Dataset

→ Sentence Embeddings

→ Logistic Regression Classifier

→ Risk Prediction

→ Chatbot Response

→ Web Application

```



\---



\# 📊 Emotional Classification Logic



The model was trained to distinguish between:



\## Neutral

Routine recovery discussion, ordinary conversation, grounded emotional states.



\## Negative

Emotional distress, overwhelm, frustration, sadness, or exhaustion without escalation intent.



\## High Risk

Relapse intent, surrender language, hopelessness, or emotionally escalated substance-use statements.



The dataset was iteratively refined to improve contextual understanding and reduce false classifications.



\---



\# 💻 Example Predictions



\### Neutral Example

Input:

```text

I went to group today and felt okay.

```



Prediction:

```text

Neutral

```



\---



\### Negative Example

Input:

```text

This is the worst day ever. I feel overwhelmed.

```



Prediction:

```text

Negative

```



\---



\### High Risk Example

Input:

```text

I give up. I'm having a drink tonight.

```



Prediction:

```text

High Risk

```



\---



\# 🖼 screenshots



\## Application Homepage

!\[Homepage](screenshots/homepage.png)



\## Negative Classification Example

!\[Negative Example](screenshots/negative.png)



\## High Risk Classification Example

!\[High Risk Example](screenshots/high_risk.png)



\---



\# 📂 Project Structure



```text

my\_first\_project/



│ app.py

│ train.py

│ predict.py

│ dataset.csv

│ model.pkl

│ label\_encoder.pkl

│ README.md

│ requirements.txt



└── Screenshots/

```



\---



\# ⚠️ Disclaimer



This project is an educational NLP and machine learning application.



It is not a replacement for professional mental health, medical, or crisis support.



\---



\# 🔮 Future Improvements



\- Expanded dataset training

\- Improved contextual understanding

\- Memory and conversational context

\- Enhanced UI/UX design

\- Public cloud deployment

\- Advanced chatbot dialogue flow



\---



\# 👤 Author



Laurie Baldwin



AI / NLP Developer  

Psychology-Oriented Systems \& Recovery-Focused Technology



