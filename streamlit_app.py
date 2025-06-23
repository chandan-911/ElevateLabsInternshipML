# streamlit_app.py

import streamlit as st
import joblib
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLP tools
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Load trained model
try:
    model = joblib.load("career_recommender.pkl")
except Exception as e:
    st.error("⚠️ Model not found. Make sure 'career_recommender.pkl' is in the same folder.")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="AI Career Recommender", page_icon="🎓")
st.title("🎓 AI Career Recommender")
st.markdown("Enter your **interests and skills**, and get a personalized career suggestion.")

# Optional predefined examples
example_inputs = [
    "I love coding and AI", "Drawing and animation", "Biology and human anatomy",
    "Business management and finance", "Graphic design", "Marketing and content writing",
    "Mechanical engineering", "App development", "Healthcare", "Teaching and mentoring"
]

with st.expander("🔍 Try example inputs"):
    cols = st.columns(3)
    for i, example in enumerate(example_inputs):
        with cols[i % 3]:
            if st.button(example):
                st.session_state['user_input'] = example

# Main input box
user_input = st.text_area("✍️ Describe your interests and skills:", key="user_input")

# Predict button
if st.button("🚀 Get Career Recommendation"):
    if user_input.strip():
        processed = preprocess(user_input)
        prediction = model.predict([processed])[0]
        confidence = model.predict_proba([processed]).max()
        st.success(f"🎯 Recommended Career: **{prediction}** ({confidence:.2%} confidence)")
        st.success(f"🎯 Recommended Career: **{prediction}**")
    else:
        st.warning("⚠️ Please enter your interest or choose an example.")
