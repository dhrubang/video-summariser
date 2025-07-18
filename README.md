# 🎥 Phidata Video AI Summarizer Agent

A powerful multimodal AI application that combines video analysis with voice input to provide intelligent insights about video content. Built with Streamlit, Phidata, and Google's Gemini AI model.

## ✨ Features

- **Video Upload & Analysis**: Upload MP4, MOV, or AVI files for AI-powered content analysis
- **Voice Input**: Record audio queries using your microphone with automatic speech-to-text transcription
- **Multimodal AI**: Leverages Google's Gemini 2.0 Flash model for advanced video understanding
- **Web Research**: Integrates DuckDuckGo search for supplementary information
- **Interactive Interface**: Clean, user-friendly Streamlit interface
- **Real-time Processing**: Live video processing with progress indicators

## 🚀 Demo

![Video Summarizer Demo](https://via.placeholder.com/800x400?text=Video+Summarizer+Demo)

## 📋 Requirements

- Python 3.8+
- Google AI API Key
- Microphone (for voice input feature)
- Webcam or video files for analysis

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dhrubang/video-summariser.git
cd video-summariser
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add your Google API key to the `.env` file:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## 🔑 Getting Your Google API Key

1. Go to the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key
5. Add it to your `.env` file as shown above

**Note**: Keep your API key secure and never commit it to version control.

## 📦 Dependencies

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
phidata>=2.4.0
google-generativeai>=0.3.0
SpeechRecognition>=3.10.0
python-dotenv>=1.0.0
pathlib>=1.0.0
pyaudio>=0.2.11
```

## 🎯 Usage

### 1. Start the Application

```bash
streamlit run app.py
```

### 2. Access the Interface

Open your browser and navigate to:
```
http://localhost:8501
```

### 3. Using the Application

1. **Upload Video**: Click "Browse files" and select your video file (MP4, MOV, or AVI)
2. **Enter Query**: 
   - Type your question in the text area, OR
   - Click the 🎙️ Record button to use voice input
3. **Analyze**: Click "🔍 Analyze Video" to process your request
4. **View Results**: The AI will provide detailed insights based on your query

## 🎤 Voice Input Feature

The application includes speech-to-text functionality:

- Click the "🎙️ Record" button to start recording
- Speak your question clearly
- The system will automatically transcribe your speech
- Review and edit the transcription if needed

## 🔧 Configuration

### Audio Settings

If you encounter audio issues, you may need to install additional audio dependencies:

**On Windows:**
```bash
pip install pyaudio
```

**On macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**On Linux:**
```bash
sudo apt-get install python3-pyaudio
```

## 📁 Project Structure

```
video-summariser/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your Google API key secure
- The application processes videos locally before sending to Google AI
- Temporary files are created during processing but not permanently stored

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Google API key is correctly set in the `.env` file
2. **Audio Issues**: Install pyaudio and check microphone permissions
3. **Video Upload Fails**: Ensure video file is in supported format (MP4, MOV, AVI)
4. **Slow Processing**: Large video files may take longer to process

### Error Messages

- `No speech detected`: Speak closer to the microphone or in a quieter environment
- `Could not understand audio`: Try speaking more clearly or use text input
- `API key not found`: Check your `.env` file configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Phidata](https://phidata.com/) for the AI agent framework
- [Google AI](https://ai.google/) for the Gemini model
- [Streamlit](https://streamlit.io/) for the web interface
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for audio processing

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/dhrubang/video-summariser/issues) page
2. Create a new issue with detailed description
3. Include error messages and system information

## 🔄 Updates

Stay updated with the latest features and bug fixes by watching this repository and pulling the latest changes regularly.

---

**Made with ❤️ by [Dhrubang](https://github.com/dhrubang)**
