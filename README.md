# Introduction

Like many people, I'm not a huge fan of clickbait. Scrolling through YouTube, you often encounter
video titles that strike a perfect balance between being interesting enough to spark your curiosity,
but vague enough to make you watch a ten minute video to be able to satisfy it.

If you think about it, every clickbait title does the same thing: whether directly or indirectly, they
get your attention by posing an interesting question. Let's take a sample from Tom Scott's recent 
videos to illustrate this:

- The broken building that must not be destroyed
- Why Australia bottles up its air.
- These chickens save lives.

Why can't the building be destroyed? Are the Australians hoarding our air? Have the chickens found a solution to the climate crisis?

Finding the answers to these questions would take you around 20 minutes of watching. But what
if you could get the answers to all these (implicit) questions within a few seconds?

Luckily, we can now let large language models bite the bait for us. By cleverly using OpenAI's GPT3, we can
identify the implicit question that sparks our curiosity and find out what the creators answer to that question is.

This project leverages OpenAI's GPT3 to do exactly that, while providing a Streamlit-powered front end. 

# Try it yourself
[Go to this application on Streamlit Cloud](https://mennoliefstingh-bait-biter-streamlit-29cy1g.streamlit.app/)

To run the application locally, you need to [generate an OpenAI API key](https://openai.com/join/). 
After obtaining one, clone the project and open the project folder in your terminal. From there:
- Create a virtual environment: `python3 -m venv env`
- Activate it: `source env/bin/activate`
- Install dependencies: `pip -r requirements.txt`
- Store your API key as an environment variable: `export OPENAI_API_KEY=[your key]`
- Run the app: `streamlit run streamlit_app.py`