import requests
import streamlit as st
from openai.error import InvalidRequestError

from bait_biter import _results, _ui_text
from bait_biter._clickbait_video import ClickbaitVideo


class BaitBiterStreamlitApp:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._answer_model_type = "text-davinci-003"

    def run_app(self):
        st.title("BaitBiter")

        with open("bait_biter/custom_html/github_button.html") as github_button_html:
            st.components.v1.html(github_button_html.read(), width=200, height=40)

        intro = st.empty()
        intro.markdown(_ui_text.intro_text)

        video_url = st.text_input("Enter a YouTube URL:")

        # Only draw live results after input has been given
        if video_url:
            intro.markdown(_ui_text.url_supplied)
            try:
                video = ClickbaitVideo(video_url, self._api_key)
                try:
                    answer = video.answer_title_question()
                    _results.display_results(video.title, video.video_id, video.question, answer)

                except InvalidRequestError as error:
                    st.write(_ui_text.openai_error_msg(error))

            except requests.JSONDecodeError:
                st.write("Looks like that's not a valid YouTube URL")
            except BaseException as error:
                st.write(error)
        else:
            _results.display_example_results()
    
