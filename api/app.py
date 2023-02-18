import os

from fastapi import FastAPI
from pydantic import BaseModel

from src._clickbait_solver import ClickbaitVideo

app = FastAPI()

api_key = os.getenv("OPENAI_API_KEY")


class YouTubeURL(BaseModel):
    url: str


@app.post("/baitbiter_api")
def extract_video_info(yt_url: YouTubeURL):
    video = ClickbaitVideo(yt_url.url, api_key)

    return {
        "title": video.title,
        "question": video.question,
        "answer": video.answer_title_question(),
    }
