import requests
from bs4 import BeautifulSoup
import re
from chatbot.core import translate_to_romaji


WIKI_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

TRUSTED_SITES = [
    "https://www.geeksforgeeks.org",
    "https://www.w3schools.com/",
    "https://www.tpointtech.com/"
]

def clean_text(text):
    # Fix common merged words like 'machine learningthat' -> 'machine learning that'
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Remove words like "Notifications" (case-insensitive)
    text = re.sub(r'\bNotifications\b', '', text, flags=re.IGNORECASE)
    # Remove excessive newlines and spaces
    text = re.sub(r'\n+', '\n', text).strip()
    return text

def format_text_as_points(text):
    # Split text into sentences by '.', '!', '?' followed by space or end of text
    sentences = re.split(r'(?<=[.!?])\s+', text)
    points = []
    for i, sentence in enumerate(sentences, 1):
        if sentence.strip():
            points.append(f"{i}. {sentence.strip()}")
    return "\n\n".join(points)

def fetch_wikipedia_summary(query):
    try:
        url = WIKI_API_URL + query.replace(" ", "_")
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return None
        data = response.json()
        return data.get("extract")
    except Exception:
        return None

def fetch_page_summary(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')

        paragraphs = soup.find_all('p')
        text = ""
        for p in paragraphs:
            paragraph_text = p.get_text(separator=" ", strip=True)
            if paragraph_text:
                text += paragraph_text + "\n\n"
            if len(text) > 600:  # Slightly longer to get full sentences
                break

        cleaned_text = clean_text(text)
        formatted_text = format_text_as_points(cleaned_text)
        return formatted_text

    except Exception:
        return None

def perform_web_tool_search(query):
    wiki_summary = fetch_wikipedia_summary(query)
    if wiki_summary:
        cleaned = clean_text(wiki_summary)
        formatted = format_text_as_points(cleaned)
        romaji = translate_to_romaji(formatted)
        if romaji:
            return {
                "type": "dual_language",
                "content": {
                    "english": f"🌐 From Wikipedia:\n\n{formatted}",
                    "romaji": romaji
                }
            }
        else:
            return {
                "type": "text",
                "content": f"🌐 From Wikipedia:\n\n{formatted}"
            }

    for site in TRUSTED_SITES:
        guess_url = f"{site}/{query.replace(' ', '-').lower()}"
        summary = fetch_page_summary(guess_url)
        if summary:
            romaji = translate_to_romaji(summary)
            if romaji:
                return {
                    "type": "dual_language",
                    "content": {
                        "english": f"🌐 From {guess_url}:\n\n{summary}",
                        "romaji": romaji
                    }
                }
            else:
                return {
                    "type": "text",
                    "content": f"🌐 From {guess_url}:\n\n{summary}"
                }

    return {
        "type": "text",
        "content": "Sorry, couldn't fetch detailed info from trusted websites."
    }
