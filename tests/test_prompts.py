# flake8: noqa
import bait_biter


def test_answer_question_prompt():
    assert (
        bait_biter.prompts.answer_question_prompt("this_is_a_transcript", "this_is_a_question")
        == """
            I will give you a transcript of a YouTube video. Afterwards, I will ask you a question 
            about this video. You will use the transcript to summarize this video and answer the question in 60 words or less.
            Transcript: [this_is_a_transcript]

            Question: [this_is_a_question]
            Three sentence summarization and answer (60 words or less): """
    )


def test_question_from_title_prompt():
    assert (
        bait_biter.prompts.question_from_title_prompt()
        == """
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
    )
