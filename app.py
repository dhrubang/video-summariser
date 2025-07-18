import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import speech_recognition as sr
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Page configuration
st.set_page_config(
    page_title="Multimodal AI Agent - Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

st.title("Phidata Video AI Summarizer Agent")

# Initialize speech recognizer
recognizer = sr.Recognizer()

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

# Initialize the agent
multimodal_agent = initialize_agent()

# File uploader with unique key
video_file = st.file_uploader(
    "Upload a video file",
    type=['mp4', 'mov', 'avi'],
    help="Upload a video for AI analysis",
    key="video_uploader"
)

# Session state for audio recording
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'transcribed_text' not in st.session_state:
    st.session_state.transcribed_text = ""

def toggle_recording():
    if not st.session_state.recording:
        # Start recording
        st.session_state.recording = True
        st.session_state.transcribed_text = ""  # Reset previous transcription
        st.info("Recording... Speak now.")
    else:
        # Stop recording and transcribe
        st.session_state.recording = False
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
                temp_audio.write(audio.get_wav_data())
                audio_path = temp_audio.name
            try:
                with sr.AudioFile(audio_path) as source:
                    audio_data = recognizer.record(source)
                    st.session_state.transcribed_text = recognizer.recognize_google(audio_data)
                st.success("Recorded! Transcription completed.")
            finally:
                Path(audio_path).unlink(missing_ok=True)
        except sr.WaitTimeoutError:
            st.error("No speech detected within the timeout period.")
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except Exception as e:
            st.error(f"An error occurred during transcription: {e}")

if video_file:
    # Save the uploaded video to a temporary file for processing
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.video(video_path, format="video/mp4", start_time=0)

    # Audio recording controls
    st.subheader("Query Input")
    if st.button("🎙️ Record", key="toggle_recording_button"):
        toggle_recording()

    # Text area for query input (populated by transcription or manual input)
    user_query = st.text_area(
        "What insights are you seeking from the video?",
        value=st.session_state.transcribed_text,
        placeholder="Ask anything about the video content, or use the audio recording feature.",
        help="Provide specific questions or insights you want from the video, or record your query using the button above.",
        key="query_input"
    )

    if st.button("🔍 Analyze Video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter or record a question or insight to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Upload and process video file
                    processed_video = upload_file(video_path)
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

                    # Prompt generation for analysis
                    analysis_prompt = (
                        f"""
                        Analyze the uploaded video for content and context.
                        Respond to the following query using video insights and supplementary web research:
                        {user_query}

                        Provide a detailed, user-friendly, and actionable response.
                        """
                    )

                    # AI agent processing
                    response = multimodal_agent.run(analysis_prompt, videos=[processed_video])

                # Display the result
                st.subheader("Analysis Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
            finally:
                # Not deleting the temporary video file as requested
                # Note: Retaining temporary files may lead to storage accumulation; consider manual cleanup or session-based storage
                pass
else:
    st.info("Upload a video file to begin analysis.")

# Customize text area height
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)