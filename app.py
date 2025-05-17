from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO, emit
from chatbot.core import get_bot_response
from chatbot.image_text import extract_text_from_image
from chatbot.web_search import perform_web_tool_search as perform_web_search

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def respond():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)

    # If the local bot fails (returns None or empty), fallback to web search
    if not bot_response or not bot_response.get("content"):
        bot_response = perform_web_search(user_message)

    return jsonify(bot_response)

@app.route("/scan_image", methods=["POST"])
def scan_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided!"}), 400

    image_data = request.files['image'].read()
    extracted_text = extract_text_from_image(image_data)

    if not extracted_text:
        return jsonify({"error": "Failed to extract text from image."}), 500

    bot_response = get_bot_response(extracted_text)

    # Fallback to web search if image text has no local match
    if not bot_response or not bot_response.get("content"):
        bot_response = perform_web_search(extracted_text)

    return jsonify(bot_response)

# ✅ New route for frontend Web Search button
@app.route("/web_search", methods=["POST"])
def web_search():
    query = request.json.get("query")
    if not query:
        return jsonify({"error": "No query provided."}), 400
    result = perform_web_search(query)
    return jsonify(result)

if __name__ == "__main__":
    socketio.run(app, debug=True)
