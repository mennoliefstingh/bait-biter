import os

import openai
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_gpt3_summary(title, transcript):

    completion = openai.Completion.create(
        model="text-curie-001",
        prompt=f"""
    This is a transcript of a YouTube video: \n {transcript} \n
    The title of the video is {title}. Explain what happens in the video and make sure the explanation relates to the title.
    Explanation: """,
        max_tokens=100,
    )
    return completion.choices[0].text


def title_to_question(title) -> str:
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
    The title of a YouTube video is [{title}]. Think of the first question that comes to mind when reading this title.
    I will now list a few examples of how these questions can arise from titles:
    When a title says that something has changed but does not specify why it changed, a logical question is what the reason for that change is.
     Answer: """,
        max_tokens=100,
    )

    print("Title: ", title)
    print("Question: ", completion.choices[0].text)
    return completion.choices[0].text


def answer_question_with_transcript(
    question: str, transcript: str, gpt_model: str = "text-curie-001"
) -> str:
    completion = openai.Completion.create(
        model=gpt_model,
        prompt=f"""
    I will give you a transcript of a YouTube video. Afterwards, I will give you a question pertaining to this video. You will answer this question. 
    Transcript: [{transcript}]

    Question: [{question}]
     Answer: """,
        max_tokens=100,
    )
    return completion.choices[0].text


def get_video_id(yt_url: str) -> str:
    return yt_url.split("=")[-1].split("?")[0]


def get_title(video_id: str) -> str:
    response = requests.get(
        f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    )
    data = response.json()
    return data["title"]


def get_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return TextFormatter().format_transcript(transcript).replace("\n", " ")


def explain_title(video_url):

    video_id = video_url.split("=")[-1]

    response = requests.get(f"https://www.youtube.com/oembed?url={video_url}&format=json")
    data = response.json()
    video_title = data["title"]

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    transcript = TextFormatter().format_transcript(transcript).replace("\n", " ")

    explanation = get_gpt3_summary(video_title, transcript)

    return video_title, explanation


# print(explain_title("https://www.youtube.com/watch?v=EqwasBTzZS8"))

video_url = "https://www.youtube.com/watch?v=q6rnzOGhj-8"
video_id = get_video_id(video_url)
title = get_title(video_id)
transcript = get_transcript(video_id)
question = title_to_question(title)
answer = answer_question_with_transcript(question, transcript, gpt_model="text-davinci-003")

print(f"The title of this video is {title}\n")
print(f"Generated question: {question}\n")
print("If you don't want to watch, the answer is:\n")
print(answer)
