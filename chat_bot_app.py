import streamlit as st
from chat_bot_component import run_youtube_chatbot
from chat_bot_component import generate_transcript_summary

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

st.markdown("---")
st.subheader("📄 Transcript Summary")

if st.button("Generate Transcript Summary"):
    if not youtube_url:
        st.warning("Please enter a YouTube video URL first.")
    else:
        with st.spinner("Generating transcript summary..."):
            try:
                _, transcript = run_youtube_chatbot(
                    youtube_url,
                    "Summarize the video"
                )

                summary = generate_transcript_summary(transcript)

                st.success("Summary generated!")
                st.write(summary)

            except Exception as e:
                st.error(f"Error: {e}")
