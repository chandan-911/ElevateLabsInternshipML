# streamlit_app.py

import streamlit as st
import joblib
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize text preprocessing tools
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Load model
try:
    model = joblib.load("career_recommender.pkl")
except Exception as e:
    st.error("⚠️ Could not load model. Make sure 'career_recommender.pkl' exists in the same folder.")
    st.stop()

# ---------- UI Configuration ----------
st.set_page_config(page_title="AI Career Recommender", page_icon="🎓")
st.title("🎓 AI Career Recommender")
st.markdown("Describe your **interests or skills**, or click an example below:")

# Initialize session state for user input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ---------- Example Buttons ----------
example_inputs = [
    "I enjoy coding and building websites",
    "I love designing posters and editing videos",
    "I am good at mathematics and accounting",
    "I want to help patients and work in hospitals",
    "I am passionate about drawing and painting",
    "I enjoy solving business problems",
    "I like studying biology and anatomy",
    "I am interested in cloud computing",
    "I love working with financial data",
    "I want to become a mechanical engineer",
    "I enjoy writing stories and blogging",
    "I like AI and machine learning",
    "I want to become a data scientist",
    "I am good at marketing and branding",
    "I enjoy working with electronics",
    "I want to manage people and lead teams",
    "I like editing reels and video content",
    "I want to explore space science",
    "I love working on cars and machines",
    "I want to start my own business"
]

cols = st.columns(4)
for i, example in enumerate(example_inputs):
    with cols[i % 4]:
        if st.button(example[:30] + "..."):
            st.session_state.user_input = example

# ---------- Text Input Area ----------
user_input = st.text_area("✍️ Or type your own input:", value=st.session_state.user_input, key="user_input")

# ---------- Submit Button ----------
if st.button("🔍 Get Career Recommendation"):
    if user_input.strip():
        processed = preprocess(user_input)
        prediction = model.predict([processed])[0]
        cleaned_output = prediction.replace("/", " at ").title()
        st.success(f"🎯 Recommended Career: **{cleaned_output}**")
    else:
        st.warning("⚠️ Please enter something or click an example above.")
