"""
Behold the Medusa of Code Snippets, the Pandora's Box of Programming, the Gordian Knot of Scripts!

This unconventional, perplexing, and downright bizarre script does something so audacious, so daring, that it should come with its own health warning:

It renames itself while running.

Yes, you heard it right. It's like a spy changing identities mid-mission, a superhero swapping costumes in a phone booth, or a chameleon changing colors on a disco floor.

Is it a bird? Is it a plane? No, it's `streamlit.py`! Wait, now it's `temp.py`!
Faster than a speeding bullet, more powerful than a locomotive, able to leap tall buildings in a single bound, this script will leave you wondering: "Where did `streamlit.py` go?"
But tread carefully, brave coder, for here be dragons.
This script laughs in the face of convention, dances on the edge of the precipice, teeters on the brink of disaster.
If interrupted, it may leave behind a mystery worthy of Sherlock Holmes: The Case of the Missing `streamlit.py`.

Why, you ask, does this script undertake such a perilous journey?
The answer lies in the pre-configured Streamlit cloud app, which insists on running `streamlit.py`.
However, the existence of a `streamlit.py` file throws a wrench in the gears of our `BaitBiterStreamlitApp`'s imports.
And so, like a heroic knight facing a fire-breathing dragon, our script must change its name, if only for a moment, to save the day.

So, strap in, hold onto your hats, and keep your arms and legs inside the vehicle at all times. This is going to be a wild ride!

Remember: with great power comes great responsibility. Use it wisely.

You have been warned.
"""

import os


def rename_file(old_name, new_name):
    # The directory of the current script
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # The full paths of the old and new filenames
    old_path = os.path.join(current_dir, old_name)
    new_path = os.path.join(current_dir, new_name)

    # Rename the file
    os.rename(old_path, new_path)


# Rename streamlit.py to temp.py
#rename_file("streamlit.py", "temp.py")

from bait_biter.streamlit_app import BaitBiterStreamlitApp

# Rename temp.py back to streamlit.py
#rename_file("temp.py", "streamlit.py")

app = BaitBiterStreamlitApp(os.getenv("OPENAI_API_KEY"))

app.run_app()
