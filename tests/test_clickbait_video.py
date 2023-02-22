import pytest
from bait_biter._clickbait_video import ClickbaitVideo


class MockCompletionResponse:
    def __init__(self, text):
        class Choices:
            def __init__(self, text):
                self.text = text

        choice_class = Choices(text)
        self.choices = [choice_class]


@pytest.fixture(autouse=True)
def mock_openai_completion(monkeypatch):
    def mock_completion(*args, **kwargs):
        return MockCompletionResponse("mock response")

    monkeypatch.setattr("openai.Completion.create", mock_completion)


@pytest.fixture
def clickbait_video():
    # use goofy ah video to test transcripts etc
    return ClickbaitVideo("https://www.youtube.com/watch?v=ICcgwifczXw", "mock_api_key")


def test_clickbait_video_title(clickbait_video):
    assert clickbait_video.title == "Alex studying - modern family funny clip"


def test_clickbait_video_id(clickbait_video):
    assert clickbait_video.video_id == "ICcgwifczXw"


def test_video_transcript(clickbait_video):
    with open("tests/sample_transcript.txt", "r") as t:
        assert clickbait_video.transcript == t.read()


def test_answer_model_type(clickbait_video):
    assert clickbait_video.answer_model_type == "text-davinci-003"


def test_api_key(clickbait_video):
    assert clickbait_video.api_key == "mock_api_key"


def test_generated_question(clickbait_video):
    assert clickbait_video.question == "mock response"


def test_video_answer_generation(clickbait_video):
    assert clickbait_video.answer_title_question() == "mock response"
