# AI Personal Assistant Chatbot 🧠💬

An intelligent and interactive AI-powered chatbot designed to assist with technical and HR interview preparation. This project combines multiple AI/ML techniques into a seamless web application for real-time interview simulation, research, and transcription.

🚀 Features
✅ Ask technical and HR questions
✅ Answers from local dataset (technical.json / hr.json)
✅ Fallback to Web Search if no local match found
✅ Supports English and Japanese (Romaji) responses
✅ Upload images and extract text (OCR)
✅ Screen sharing with system audio capture
✅ Real-time transcription of system audio
✅ Automatic detection of questions in transcribed audio and response generation
✅ User-friendly chat interface

🧠 Tech Stack
Python (Flask)

JavaScript (Vanilla + Media APIs)

HTML/CSS (Frontend UI)

Vosk (Offline Speech Recognition)

FFmpeg (System Audio Extraction)

DuckDuckGo (Web Search via API)

EasyOCR / Tesseract (for image text extraction)

JSON-based QA Dataset

📦 Folder Structure
AI_ChatBot/
│
├── app.py                        # Main Flask application
├── chatbot/
│   ├── core.py                  # Core chatbot logic (local + Romaji + fallback)
│   ├── image_text.py           # OCR functions
│   ├── web_search.py           # Web search fallback logic
│   └── utils.py                # Helper functions
│
├── static/
│   ├── style.css               # Frontend styling
│   └── script.js               # Screen sharing, audio recording, transcription
│
├── templates/
│   └── index.html              # Chatbot UI
│
├── technical.json              # Technical interview Q&A dataset
├── hr.json                     # HR interview Q&A dataset
├── requirements.txt            # All required Python dependencies
└── README.md                   # You are here ✅
📸 Screenshots
Coming soon…

🔧 Installation
Clone this repo:

git clone https://github.com/YujiItaori/AI_ChatBot.git
cd AI_ChatBot
Install dependencies:

pip install -r requirements.txt
Make sure you have FFmpeg installed on your system and available in PATH.

Run the app:
![Screenshot 2025-05-17 110805](https://github.com/user-attachments/assets/fbacd7ee-da4c-4223-a138-42806c634e6d)
![Screenshot 2025-05-17 110824](https://github.com/user-attachments/assets/b9065008-d1b7-4ffc-8a7b-620fdaf0b860)

python app.py
Navigate to http://localhost:5000 in your browser.

🗣 Usage Guide
Ask any question via the chat input. The bot will respond from the local dataset or fallback to a web search.

Upload an image with embedded text — it will extract and answer any question-like text.

Click “Share Screen” to share your screen and system audio.

The bot transcribes any audio (e.g., an interviewer’s voice) in real time, detects questions, and provides answers instantly.

🌐 Languages Supported
English

Japanese (Romaji) – Example: "kagaku teki shikou wa nani?"

📁 Datasets
technical.json – Core AI/ML/DS coding & theory questions

hr.json – Soft skills, behavioral questions, job expectations, etc.

You can customize these JSON files to suit your domain!

🛡️ Privacy Note
All processing is done locally — no audio/video is sent to external servers. Web search is anonymous via DuckDuckGo.

📌 Future Improvements
Real-time sentiment analysis

Multilingual audio recognition (Hindi, Japanese)

PDF/CV content parsing

Interview scoring & analytics dashboard

👨‍💻 Author
Made with ⚡ by Yash Vishwas

GitHub: YujiItaori

📜 License
MIT License

Let me know if you want a Japanese-translated README or a shorter GitHub Summary section!
