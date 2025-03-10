# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GA7BhuG2UVu7SFtNI98K3yTWm9-OzY4c
"""

!pip install streamlit whisper openai-whisper pyngrok

import streamlit as st
import whisper
import tempfile
import os
import requests
from urllib.parse import urlparse
from pyngrok import ngrok

# Load the Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Function to download file from URL
def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_file.write(response.content)
            return tmp_file.name
    return None

# Streamlit app
st.set_page_config(page_title="Whisper AI - Speech to Text", page_icon="🎙️", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎙️ Whisper AI - Speech to Text")
st.write("Upload an audio/video file or provide a URL to convert speech to text.")

# File upload and URL input
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Choose a file", type=["wav", "mp3", "mp4", "m4a"])

with col2:
    url = st.text_input("Or enter a URL to an audio/video file")

if uploaded_file is not None or url:
    if st.button("Transcribe"):
        with st.spinner("Transcribing..."):
            try:
                if uploaded_file:
                    # Save the uploaded file to a temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        tmp_file_path = tmp_file.name
                elif url:
                    # Download file from URL
                    tmp_file_path = download_file(url)
                    if not tmp_file_path:
                        st.error("Failed to download the file from the provided URL.")
                        st.stop()

                # Transcribe the audio
                transcription = model.transcribe(tmp_file_path)

                # Display results
                st.subheader("Transcription Result:")
                st.write(transcription["text"])

                # Display additional information
                st.subheader("Additional Information:")
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Detected Language:** {transcription['language']}")
                with col2:
                    st.write(f"**Confidence:** {transcription['segments'][0]['confidence']:.2f}")

                # Clean up the temporary file
                os.remove(tmp_file_path)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built by: Syed Fasih Zaidi")

# Set up ngrok
ngrok.set_auth_token("2scPSRtkxxSvQ2tWhmjdbRviNWv_3j3KMb762mD8X1PmyhkoQ") # Replace with your auth token

# Terminate existing tunnels if necessary
try:
    # Get a list of all active tunnels
    tunnels = ngrok.get_tunnels()
    # Disconnect each tunnel
    for tunnel in tunnels:
        ngrok.disconnect(tunnel.public_url)
except:
    pass


# Run the Streamlit app
!streamlit run app.py &>/dev/null&

# Set up ngrok tunnel
public_url = ngrok.connect(addr="8501")
print(f"Streamlit app is live at: {public_url.public_url}")