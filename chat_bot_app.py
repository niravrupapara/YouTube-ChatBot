import streamlit as st
from chat_bot_component import run_youtube_chatbot

st.set_page_config(
    page_title="YouTube ChatBot",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 YouTube Video ChatBot")
st.write("Ask questions about any YouTube video using AI.")

# Input fields
youtube_url = st.text_input(
    "Enter YouTube Video URL",
    placeholder="https://youtu.be/..."
)

question = st.text_area(
    "Ask a question about the video",
    placeholder="What is this video about?"
)

# Button
if st.button("Get Answer"):
    if not youtube_url or not question:
        st.warning("Please enter both YouTube URL and question.")
    else:
        with st.spinner("Processing video and generating answer..."):
            try:
                answer = run_youtube_chatbot(youtube_url, question)
                st.success("Answer generated!")
                st.markdown("### ✅ Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
