# flake8: noqa

intro_text = """
        Like many people, I'm not a huge fan of clickbait. Scrolling through YouTube, you often encounter
        video titles that strike a perfect balance between being interesting enough to spark your curiosity,
        but vague enough to make you watch a ten minute video to be able to satisfy it.

        If you think about it, every clickbait title does the same thing: whether directly or indirectly, they
        get your attention by posing an interesting question. Let's take a sample from Tom Scott's recent 
        videos to illustrate this:

        - The broken building that must not be destroyed
        - Why Australia bottles up its air.
        - These chickens save lives.

        Why can't the building be destroyed? 
        Are the Australians hoarding our air? Have the chickens found a solution to the climate crisis?

        Finding the answers to these questions would take you around 20 minutes of watching. But what
        if you could get the answers to all these (implicit) questions within a few seconds?

        Luckily, we can now let large language models bite the bait for us. By cleverly using OpenAI's GPT3, we can
        identify the implicit question that sparks our curiosity and find out what the creators answer to that question is.
        See a demo of the results for Tom Scott's video, or try it yourself by pasting a link to a video in the field below.

        Update (22-02-2023):
        - Video transcripts are now stemmed and stopwords are removed before passing them to GPT-3, allowing for longer videos to be analyzed!

        Update (29-07-2023):
        - Finally updated this to use gpt-3.5 🥲
        - Extremely long transcripts are now split up, sections are summarized and joined back together. Theoretically, this should allow for videos of any length to be analyzed. 
    """

password_correct = """
        Super secret password correct! The next query will use the more advanced (and expensive)
        davinci model to answer the video's implicit question.
    """


def openai_error_msg(error) -> str:
    return f"""
        OpenAI returned an error: 

        Error message: *{error}*
    """


url_supplied = """
        Nice job! If (when) you find any errors or weird behavior, let me know by \
        [creating an issue on GitHub](https://github.com/mennoliefstingh/bait-biter/issues/new/choose).
    """
