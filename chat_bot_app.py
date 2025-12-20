import streamlit as st
from chat_bot_component import get_video_transcript , answer_from_transcript , generate_transcript_summary

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "summary" not in st.session_state:
    st.session_state.summary = None


st.set_page_config(
    page_title="Youtube Chatbot" , 
    page_icon="🎥" , 
    layout='centered'
)

st.title("🎥 YouTube Video ChatBot")

st.write("this app will let chat with any youtube video")


youtube_url = st.text_input("Enter YouTube Video URL" , placeholder="https://youtu.be/xxxxxxxxxxx")

if st.button("generate Summary"):
    if not youtube_url:
        st.warning("please Enter Youtube Link")
    else:
         with st.spinner("Fetching Transcript and Generating Summary"):
             transcript = get_video_transcript(youtube_url)
             summary = generate_transcript_summary(transcript)

             st.session_state.transcript = transcript
             st.session_state.summary = summary

if st.session_state.summary:
    st.subheader("📄 Video Summary")
    st.write(st.session_state.summary)


if st.session_state.summary:
    st.subheader("💬 Ask a Question")

    user_question = st.text_input(
        "Enter your question about the video"
    )

    if st.button("Ask Question"):
        if not user_question:
            st.warning("Please enter a question")
        else:
            with st.spinner("Thinking..."):
                answer = answer_from_transcript(
                    st.session_state.transcript,
                    user_question
                )

                st.subheader("✅ Answer")
                st.write(answer)
