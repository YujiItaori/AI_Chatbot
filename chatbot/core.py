import json
import joblib
import random
import logging
import numpy as np
from chatbot.utils import clean_text
from googletrans import Translator
import re
import nltk
import pykakasi
from tensorflow.keras.models import load_model

nltk.download('punkt')

model = load_model('models/chatbot_model_tf.h5')
tfidf = joblib.load('models/tfidf_vectorizer.pkl')
encoder = joblib.load('models/label_encoder.pkl')

intent_files = [
    'data/intents.json',
    'data/python.json',
    'data/machine_learning.json',
    'data/data_science.json',
    'data/deep_learning.json',
    'data/ml_math.json',
    'data/frameworks.json'
]

intents = []
for file_path in intent_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        intents.extend(json.load(f).get('intents', []))

# Load hr.json and convert to intent-like format
hr_file_path = 'data/hr.json'
try:
    with open(hr_file_path, 'r', encoding='utf-8') as f:
        hr_data = json.load(f)
        for qa in hr_data:
            intents.append({
                "tag": "hr_interview",
                "patterns": [qa["question"]],
                "responses": [qa["answer"]]
            })
except Exception as e:
    logging.error(f"Failed to load hr.json: {e}")

technical_terms = set([
    "AI", "HTML", "CSS", "Python", "Java", "TensorFlow", "PyTorch", "Machine Learning", 
    "JavaScript", "SQL", "PHP", "API", "REST", "JSON", "XML", "GitHub", "Linux", "Docker", 
    "Kubernetes", "Cloud", "Neural Network", "Deep Learning", "Blockchain", "Django", "Flask",
    "Data Science"
])

def detect_technical_terms(text):
    words = nltk.word_tokenize(text)
    capitalized_words = [word for word in words if word.istitle()]
    return set(capitalized_words) | technical_terms

def clean_romaji(text):
    text = re.sub(r'\s*([。．．.!！?？])\s*', r'\1 ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s*,\s*', ', ', text)
    text = re.sub(r'([.。])(?=\S)', r'\1 ', text)
    return text.strip()

def post_process_romaji(text):
    # Correct particle pronunciation
    text = re.sub(r'\bha\b', 'wa', text)
    text = re.sub(r'\bhe\b', 'e', text)
    text = re.sub(r'\bwo\b', 'o', text)

    # Capitalize technical terms
    for term in technical_terms:
        pattern = re.compile(r'\b' + re.escape(term.lower()) + r'\b', re.IGNORECASE)
        text = pattern.sub(term, text)
    
    return clean_romaji(text)

def translate_to_romaji(text):
    try:
        terms = detect_technical_terms(text)
        translator = Translator()
        japanese = translator.translate(text, src='en', dest='ja').text

        kakasi = pykakasi.kakasi()
        kakasi.setMode("J", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("H", "a")
        kakasi.setMode("r", "Hepburn")
        kakasi.setMode("s", True)
        converter = kakasi.getConverter()

        romaji = converter.do(japanese)
        romaji = post_process_romaji(romaji)
        sentences = re.split(r'(?<=[.!?]) +', romaji)
        return ' '.join(s.capitalize() for s in sentences)
    except Exception as e:
        logging.error(f"Romaji translation failed: {e}")
        return None

def get_response_from_intents(predicted_label):
    for intent in intents:
        if intent['tag'] == predicted_label:
            response = random.choice(intent['responses'])
            romaji = translate_to_romaji(response)
            if romaji:
                return {
                    "type": "dual_language",
                    "content": {
                        "english": response,
                        "romaji": romaji
                    }
                }
            return {"type": "text", "content": response}
    return None

def get_bot_response(user_input):
    cleaned = ' '.join(clean_text(user_input))
    input_vector = tfidf.transform([cleaned]).toarray()
    prediction = model.predict(input_vector)[0]
    index = np.argmax(prediction)
    label = encoder.inverse_transform([index])[0]
    return get_response_from_intents(label) or {
        "type": "text", "content": "Sorry, I didn't understand that."
    }
