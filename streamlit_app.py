import streamlit as st
from model import predict_mood

st.title("AI Mood Detector")

user_input = st.text_input("Enter your mood")

if st.button("Predict"):
    mood, suggestion = predict_mood(user_input)
    st.write("Mood:", mood)
    st.write("Suggestion:", suggestion)
