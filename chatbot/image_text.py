import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import io
import logging

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_data):
    try:
        image = Image.open(io.BytesIO(image_data)).convert('L')
        image = ImageEnhance.Contrast(image).enhance(2)
        image = image.filter(ImageFilter.SHARPEN)
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        logging.error(f"OCR Error: {e}")
        return None
