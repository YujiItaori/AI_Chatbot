# AI Personal Assistant Chatbot 🧠💬

An intelligent and interactive AI-powered chatbot designed to assist with technical and HR interview preparation. This project combines multiple AI/ML techniques into a seamless web application for real-time interview simulation, research, and transcription.

## 🚀 Features

- ✅ **Interactive Q&A**: Ask technical and HR questions with intelligent responses
- ✅ **Local Dataset Support**: Answers from local dataset (technical.json / hr.json)
- ✅ **Web Search Fallback**: Automatic web search if no local match found
- ✅ **Multilingual Support**: Supports English and Japanese (Romaji) responses
- ✅ **OCR Integration**: Upload images and extract text automatically
- ✅ **Screen Sharing**: Real-time screen sharing with system audio capture
- ✅ **Live Transcription**: Real-time transcription of system audio
- ✅ **Smart Detection**: Automatic question detection in transcribed audio with response generation
- ✅ **User-Friendly Interface**: Clean and intuitive chat interface

## 🧠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python (Flask)** | Backend framework |
| **JavaScript (Vanilla + Media APIs)** | Frontend interactivity |
| **HTML/CSS** | User interface |
| **Vosk** | Offline speech recognition |
| **FFmpeg** | System audio extraction |
| **DuckDuckGo API** | Web search functionality |
| **EasyOCR / Tesseract** | Image text extraction |
| **JSON** | QA dataset storage |

## 📦 Project Structure

```
AI_ChatBot/
│
├── app.py                  # Main Flask application
├── chatbot/
│   ├── core.py            # Core chatbot logic
│   ├── image_text.py      # OCR functionality
│   ├── web_search.py      # Web search integration
│   └── utils.py           # Utility functions
├── static/
│   ├── style.css          # Frontend styling
│   └── script.js          # Frontend JavaScript
├── templates/
│   └── index.html         # Main HTML template
├── technical.json         # Technical questions dataset
├── hr.json               # HR questions dataset
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Installation

### Prerequisites
- Python 3.7+
- FFmpeg (must be installed and available in PATH)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YujiItaori/AI_ChatBot.git
   cd AI_ChatBot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify FFmpeg installation**
   ```bash
   ffmpeg -version
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🗣️ Usage Guide

### Basic Chat
- Type any question in the chat input
- The bot responds from local dataset or performs web search fallback
- Supports both English and Japanese (Romaji) queries

### Image Text Extraction
- Upload an image containing text
- The system automatically extracts and processes any question-like content
- Provides relevant answers based on extracted text

### Screen Sharing & Audio Transcription
1. Click the **"Share Screen"** button
2. Select your screen and enable system audio
3. The bot transcribes audio in real-time
4. Automatically detects questions and provides instant responses

### Example Queries
- **English**: "What is machine learning?"
- **Japanese (Romaji)**: "kagaku teki shikou wa nani?"

## 🌐 Language Support

| Language | Status | Example |
|----------|--------|---------|
| **English** | ✅ Full Support | "What is artificial intelligence?" |
| **Japanese (Romaji)** | ✅ Full Support | "kagaku teki shikou wa nani?" |

## 📁 Dataset Configuration

### Technical Questions (`technical.json`)
- Core AI/ML/DS coding questions
- Theory and conceptual questions
- Algorithm explanations

### HR Questions (`hr.json`)
- Soft skills assessment
- Behavioral questions
- Job expectations and scenarios

**Customization**: You can modify these JSON files to suit your specific domain or add new categories.

## 🛡️ Privacy & Security

- **Local Processing**: All audio/video processing is done locally
- **No External Data Transfer**: Audio and video are not sent to external servers
- **Anonymous Web Search**: Web searches are conducted anonymously via DuckDuckGo
- **Data Protection**: No personal data is stored or transmitted

## 📌 Future Roadmap

- [ ] **Real-time Sentiment Analysis**: Analyze emotional responses during interviews
- [ ] **Extended Language Support**: Hindi and native Japanese audio recognition
- [ ] **PDF/CV Parsing**: Extract and analyze resume content
- [ ] **Interview Analytics**: Comprehensive scoring and performance dashboard
- [ ] **Mobile App**: Native mobile application support
- [ ] **API Integration**: RESTful API for third-party integrations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Yash Vishwas**
- GitHub: [@YujiItaori](https://github.com/YujiItaori)
- Made with ⚡ and passion for AI

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing libraries
- Special thanks to contributors and testers
- Inspired by the need for accessible interview preparation tools

---

⭐ **Star this repository if you find it helpful!** ⭐

*"The best way to predict the future is to create it." - Peter Drucker*

---

*For Japanese-translated README or additional documentation, please feel free to reach out!*
