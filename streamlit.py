from src._clickbait_solver import ClickbaitVideo
import os
import streamlit as st

api_key = os.getenv("OPENAI_API_KEY")

st.title("Counter-Clickbait Tool")

video_url = st.text_input("What is the video URL?")

if len(video_url) > 1:
    video = ClickbaitVideo(video_url, api_key)
    st.write(f"The original video title is '{video.title}'")
    st.write("From that title, GPT-3 came up with the following question:")
    st.write(video.question)

    st.write("GPT3's answer: ")
    st.write(video.answer_title_question())
