# flake8: noqa
ANSWER_QUESTION_INSTRUCTION = """
            I will now give you the transcript of a YouTube video. Use this transcript to generate a summary of the video that answers this
            question in 60 words or less. 
            """

SUMMARIZE_INSTRUCTION = """"
            You are an assistant that helps summarize YT video transcripts into a much shorter format. You will get the transcript of part of a YouTube video
            and you will summarize it in less than 100 words. """

def question_from_title_prompt(title: str) -> str:
    return f"""
        I am going to give you the clickbaity title of a YouTube video. Think of the first question that comes
        to mind when reading this title.
        I will now list a few examples of how these questions can arise from titles:
        If the title is already a clear question, return an exact to the letter copy of the title.
        When a title says that something has changed but does not specify why it changed,
        a logical question is what the reason for that change is.
        When the title indicates the status of an object, such as [thing/this] is the most [adjective],
        a logical question is why the object has that status.

        Reply with the implicit question and ONLY the implicit question. 
        """

def answer_question_prompt(transcript: str, question: str) -> str:
    return f"""
            I will give you a transcript of a YouTube video. Afterwards, I will ask you a question 
            about this video. You will use the transcript to summarize this video and answer the question in 60 words or less.
            Transcript: [{transcript}]

            Question: [{question}]
            Three sentence summarization and answer (60 words or less): """
