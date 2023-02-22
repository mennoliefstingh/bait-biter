import os

from bait_biter.streamlit_app import BaitBiterStreamlitApp

app = BaitBiterStreamlitApp(os.getenv("OPENAI_API_KEY"))

app.run_app()
