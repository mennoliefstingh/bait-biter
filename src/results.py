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
    video_id = "jOht6qmuG-k"
    video_title = "How humans disrupted a cycle essential to all life"
    implicit_question = "What caused humans to disrupt this cycle essential to all life?"
    answer = """Humans caused the disruption of Earth's cycle of life by digging up carbon that was trapped
          in the ground and putting it back into the atmosphere. This caused Earth's temperature
            to increase rapidly and risk catastrophic warming in a short 12 year span. 
            To counteract this, humans must stop emitting carbon altogether, 
            grow more plants, burn plants for energy while capturing their emissions,
              and build machines to suck out atmospheric carbon. """
    display_results(video_title, video_id, implicit_question, answer)
