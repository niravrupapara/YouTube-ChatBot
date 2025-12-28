import streamlit as st
from chat_bot_component import get_video_transcript , answer_from_transcript , generate_transcript_summary

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "video_url" not in st.session_state:
    st.session_state.video_url = None


st.set_page_config(
    page_title="Youtube Chatbot" , 
    page_icon="🎥" , 
    layout='wide' ,
    initial_sidebar_state='collapsed'
)

def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

st.markdown('<h1 class="main-header">🎥 YouTube Video ChatBot</h1>' , unsafe_allow_html=True)
st.markdown('<p class="subtitle">Chat with any YouTube Video Transcript</p>' , unsafe_allow_html=True)
col1 , col2 , col3 = st.columns([1,2,1])





with col2:

    st.markdown("### Enter YouTube Video URL")
    youtube_url = st.text_input(
        "Enter YouTube Video URL" , 
        placeholder="https://www.youtube.com/watch?v=... or https://youtu.be/..." ,
        label_visibility="collapsed",
        key="youtube_url_input")
    
    col_button1 , col_button2  = st.columns([2,1])

    with col_button1:
        summary_button = st.button("Generate Summary" , key="generate_summary_button" , use_container_width=True)

    with col_button2:
        question_button = st.button("Ask Question" , key="ask_question_button" , use_container_width=True)



    if summary_button:
        if not youtube_url:
            st.warning("Please enter a YouTube link")
        else:
            with st.spinner("Fetching Transcript and Generating Summary..."):
                transcript = get_video_transcript(youtube_url)
                summary = generate_transcript_summary(transcript)

                st.session_state.transcript = transcript
                st.session_state.summary = summary 
                st.session_state.video_url = youtube_url
                st.success("Summary Generated Successfully!")

                st.markdown("### 📄 Video Summary")
                st.markdown(f'<div class="summary-box">{st.session_state.summary}</div>' , unsafe_allow_html=True)


    if question_button:
        pass   