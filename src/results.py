import streamlit as st


def display_results(video_title: str, video_id: str, implicit_question: str, answer: str) -> None:

    col1, col2, col3 = st.columns(3)
    with col1:
        st.empty()
    with col2:
        st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", caption=video_title)
    with col3:
        st.empty()

    # st.title(f"Video title: {video_title}")
    st.write(f"**Implicit question**: {'*'+implicit_question.strip()+'*'}")
    st.write("**GPT3's answer, as extracted from the video:**")
    st.write(answer)


def display_example_results() -> None:
    st.image("https://img.youtube.com/vi/PSrO55KS6VY/0.jpg")
    st.title("These chickens save lives.")
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
