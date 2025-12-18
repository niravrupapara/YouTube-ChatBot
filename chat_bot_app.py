import streamlit as st
from chat_bot_component import get_video_transcript , answer_from_transcript
st.set_page_config(
    page_title="Youtube Chatbot" , 
    page_icon="🎥" , 
    layout='centered'
)

st.title("🎥 YouTube Video ChatBot")

st.write("this app will let chat with any youtube video")


youtube_url = st.text_input("Enter YouTube Video URL" , placeholder="https://youtu.be/xxxxxxxxxxx")

question = st.text_area("Ask a question about this video" , placeholder="What is this video about?")


if st.button("Get Answer"):
    if not youtube_url:
        st.warning("Please Enter youtube URL")

    elif not question:
        st.warning("Please Enter Question")
    else :
        with st.spinner("Processing vieo and generating answer..."):
            try:
                transcript = get_video_transcript(youtube_url)
                answer = answer_from_transcript(transcript , question)

                st.success("Answer Generated")

                st.markdown("Answer")

                st.write(answer)

            except Exception as e:
                st.error(f"Error {e}")