import os

import streamlit as st
from src._clickbait_solver import ClickbaitVideo

api_key = os.getenv("OPENAI_API_KEY")
secret_password = os.getenv("SUPER_SECRET_PASSWORD")

password_entered = False

model_type = "text-curie-001"

st.title("BaitBiter")

intro = st.empty()

intro.markdown(
    """
        Like many people, I'm not a huge fan of clickbait. Scrolling through YouTube, you often encounter
        video titles that strike a perfect balance between being interesting enough to spark your curiosity,
        but vague enough to make you watch a ten minute video to be able to satisfy it. 
        
        If you think about it, every clickbait title does the same thing: whether directly or indirectly, they
        get your attention by posing an interesting question. Let's take a sample from Tom Scott's recent 
        videos to illustrate this:
        
        - The broken building that must not be destroyed
        - I tried using AI. It scared me. 
        - Why Australia bottles up its air.
        - These chickens save lives.
        
        Why can't the building be destroyed? What scared Tom about AI? 
        Are the Australians hoarding our air? Are the chickens also paramedics?

        Other videos just ask questions directly. Is Polands water supply really protected by clams? How much helium
        does it take to lift a person?

        Finding the answers to these questions would take you around 25 minutes of watching Tom Scott videos. But what
        if you could get the answers to all these (implicit) questions within a few seconds?

        Luckily, we can now let large language models bite the bait for us. By cleverly using OpenAI's GPT3, we can 
        identify the implicit question that sparks our curiosity and find out what the creators answer to that question is.
        See a demo of the results for Tom Scott's video, or try it yourself by pasting a link to a video in the field below. 
        """
)

video_url = st.text_input("Enter a YouTube URL:")

if video_url == secret_password:
    intro.markdown(
        "Super secret password correct! Re-attempting previous query with the more advanced (and expensive) davinci model."
    )
    model_type = "text-davinci-003"

if len(video_url) > 1 and not video_url == secret_password:
    intro.markdown(
        "Nice job! If (when) you find any errors or weird behavior, let me know or create an issue on GitHub!"
    )
    video = ClickbaitVideo(video_url, api_key, answer_model=model_type)

    st.title(video.title)
    st.image(f"https://img.youtube.com/vi/{video.video_id}/0.jpg")
    st.write(f"**Implicit question**: {'*'+video.question.strip()+'*'}")
    st.write("**GPT3's answer, as extracted from the video:**")

    answer = video.answer_title_question()
    if "OpenAI returned an error, most likely because the video transcript is too long" in answer:
        st.write(
            """The video is too long for the text-curie-001 model. text-davinci-003 can handle two times as many tokens, but is also ten times as expensive.
        If you want, you can ask for the special password to unlock the larger model."""
        )
    else:
        st.write(answer)

    # reset the model type in case it was elevated
    model_type = "text-curie-001"
else:
    # display defaults
    st.title("These chickens save lives.")
    st.image("https://img.youtube.com/vi/PSrO55KS6VY/0.jpg")
    st.write("**Implicit question**: *How do these chickens save lives?*")

    st.write("**GPT3's answer, as extracted from the video:**")
    st.write(
        """The chickens help keep people in this area of New South Wales
      safe from some nasty diseases, like Murray Valley Encephalitis. It infects
        animals, including humans, and it's carried by mosquitoes. It has no vaccine, 
        no cure. Most people who get it will suffer fever and nausea, but about one
          in a thousand will get seriously ill, with a chance of life-changing brain
            injuries, or death. """
    )
