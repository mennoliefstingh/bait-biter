# flake8: noqa
def answer_question_prompt(transcript: str, question: str) -> str:
    return f"""
            I will give you a transcript of a YouTube video. Afterwards, I will ask you a question 
            about this video. You will answer this question. 
            Transcript: [{transcript}]

            Question: [{question}]
            Answer: """


def question_from_title_prompt(title: str) -> str:
    return f"""
        The title of a YouTube video is [{title}]. Think of the first question that comes
        to mind when reading this title.
        I will now list a few examples of how these questions can arise from titles:
        If the title is already a clear question, return an exact to the letter copy of the title.
        When a title says that something has changed but does not specify why it changed,
        a logical question is what the reason for that change is.
        When the title indicates the status of an object, such as [thing/this] is the most [adjective],
        a logical question is why the object has that status.
        Answer: """
