import os

import requests
import streamlit as st
from openai.error import InvalidRequestError

from src import results, ui_text
from src.clickbait_video import ClickbaitVideo

api_key = os.getenv("OPENAI_API_KEY")
secret_password = os.getenv("SUPER_SECRET_PASSWORD")

password_entered = False

# answer_model_type = "text-curie-001"
answer_model_type = "text-davinci-003"

st.title("BaitBiter")

intro = st.empty()

intro.markdown(ui_text.intro_text)

video_url = st.text_input("Enter a YouTube URL:")

if video_url == secret_password:
    intro.markdown(ui_text.password_correct)
    model_type = "text-davinci-003"

elif len(video_url) > 1:
    intro.markdown(ui_text.url_supplied)
    try:
        video = ClickbaitVideo(video_url, api_key, answer_model_type=answer_model_type)
        try:
            answer = video.answer_title_question()
            results.display_results(video.title, video.video_id, video.question, answer)
            answer_model_type = "text-curie-001"

        except InvalidRequestError as error:
            st.write(ui_text.openai_error_msg(error))

    except requests.JSONDecodeError:
        st.write("Looks like that's not a valid YouTube URL")
    except BaseException as error:
        st.write(ui_text.openai_error_msg(error))
else:
    results.display_example_results()
