import streamlit as st
from model import predict_mood

st.set_page_config(page_title="AI Mood Detector")

st.title("💬 AI Mood Detector Chatbot")

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        mood, suggestion = predict_mood(user_input)

        st.write(f"🧑 You: {user_input}")

        if mood == "Sad":
            st.error(f"😢 Mood: {mood}")
        elif mood == "Happy":
            st.success(f"😊 Mood: {mood}")
        else:
            st.info(f"😐 Mood: {mood}")

        st.write(f"💡 Suggestion: {suggestion}")
    else:
        st.warning("Please enter something")
