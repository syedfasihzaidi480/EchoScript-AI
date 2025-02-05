# EchoScript-AI
Convert Audio, and Video into Text

This is an AI-powered **Speech-to-Text** application built using **OpenAI’s Whisper model**, **Streamlit**, and **ngrok**. It allows users to **upload an audio/video file or provide a URL** to transcribe speech into text.
![1](https://github.com/user-attachments/assets/18385961-9bf1-4c44-927c-fb5f6b9fa29c)

## 🌟 Features
✅ **Supports multiple audio formats** (`.wav`, `.mp3`, `.mp4`, `.m4a`)  
✅ **URL-based transcription** (fetches audio/video from a link)  
✅ **Language detection** with confidence scores  
✅ **Interactive UI** built with Streamlit  
✅ **Accessible remotely** via ngrok  

## 🛠️ Tech Stack
- **Python**
- **Whisper AI**
- **Streamlit**
- **Ngrok**
- **Requests** (for URL-based file download)

## 🚀 Installation & Setup
Follow these steps to **set up the Whisper AI Speech-to-Text app** locally:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/syedfasihzaidi480/EchoScript-AI.git
cd EchoScript-AI
```

## 2️⃣ Install Dependencies
pip install -r requirements.txt

## 3️⃣ Run the Application
streamlit run app.py

## 4️⃣ Expose Public URL (Optional)
ngrok authtoken YOUR_NGROK_AUTH_TOKEN
ngrok http 8501

## 📝 How It Works
-Upload an audio/video file or enter a URL to fetch a file.
-Click the "Transcribe" button.
-The Whisper AI model will process the file and generate a transcription.
-View the transcription, language detected, and confidence score.
-(Optional) Share the public ngrok URL to access the app remotely.


✍️ Author
Developed by Syed Fasih Zaidi.
