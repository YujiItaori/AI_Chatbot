import spacy
import json
import random
import re

# Load spaCy's English model for text processing
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Function to clean text using spaCy."""
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def tokenizer(text):
    """Simple tokenizer function to split text into words."""
    return text.split()

# Load intents file
with open("data/intents.json", "r") as f:
    intents = json.load(f)['intents']


def summarize_by_intent(text, intent):
    # Truncate long text and split into sentences
    sentences = re.split(r'\.\s+', text.strip())[:10]

    if intent == "summarize":
        return "Summary:\n" + " ".join(sentences[:3])

    elif intent == "describe" or intent == "explain":
        return "Explanation:\n" + " ".join(sentences[:5])

    elif intent == "evaluate":
        return (
            "Evaluation:\n"
            + "Strengths: " + " ".join(sentences[:2]) + "\n"
            + "Limitations: " + " ".join(sentences[2:4])
        )

    else:
        return "Information:\n" + " ".join(sentences[:4])
