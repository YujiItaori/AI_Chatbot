    const socket = io();

    // Handle bot response (e.g., for user-typed input or web search)
    socket.on('bot_response', (data) => {
        const chatbox = document.getElementById('chatbox');
        let message;
        if (data.type === 'dual_language') {
            message = `🤖 Bot: ${data.content.english}\nRomaji: ${data.content.romaji}`;
        } else {
            message = `🤖 Bot: ${data.content}`;
        }
        const p = document.createElement('p');
        p.textContent = message;
        chatbox.appendChild(p);
    });

    // Handle transcription from speaker audio (interviewer voice)
    socket.on('transcription', (data) => {
        const chatbox = document.getElementById('chatbox');
        const p = document.createElement('p');
        p.textContent = `🧑 Interviewer: ${data.content}`;
        p.style.fontStyle = "italic";
        chatbox.appendChild(p);
    });

    // Send user message (input box)
    function sendMessage() {
        const input = document.getElementById("user_input");
        const message = input.value.trim();
        if (!message) return;

        const chatbox = document.getElementById("chatbox");
        const userMsg = document.createElement("p");
        userMsg.textContent = `🧑 You: ${message}`;
        chatbox.appendChild(userMsg);

        fetch("/get_response", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        })
            .then(res => res.json())
            .then(data => {
                // Display structured bot message (including dual language etc)
                displayStructuredMessage(data);
            })
            .catch(err => {
                console.error("Error sending message:", err);
            });

        input.value = "";
    }

    document.getElementById("send_button").addEventListener("click", sendMessage);
document.getElementById("web_search_button").addEventListener("click", triggerWebSearch);
    document.getElementById("user_input").addEventListener("keypress", e => {
        if (e.key === "Enter") sendMessage();
    });

    document.querySelector(".upload-btn").addEventListener("click", () => {
        document.getElementById("image_input").click();
    });

    document.getElementById("image_input").addEventListener("change", scanImage);

    function appendMessage(text, className) {
        const chatbox = document.getElementById("chatbox");
        const messageDiv = document.createElement("div");
        messageDiv.className = className;
        messageDiv.innerHTML = text.replace(/\n/g, "<br>");
        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function displayStructuredMessage(data) {
    const chatbox = document.getElementById("chatbox");
    const messageDiv = document.createElement("div");
    messageDiv.className = "bot-message";

    if (data.type === "dual_language") {
        messageDiv.innerHTML = `
            <div class="dual-language-response">
                <div class="english">
                    <h4>English:</h4>
                    <p>${data.content.english}</p>
                </div>
                <div class="romaji">
                    <h4>Japanese (Romaji):</h4>
                    <p>${data.content.romaji}</p>
                </div>
            </div>
        `;
    } else if (data.type === "text") {
        messageDiv.innerHTML = `<p>${data.content}</p>`;
    } else if (data.type === "list") {
        messageDiv.innerHTML = `<ul>${data.content.map(item => `<li>${item}</li>`).join('')}</ul>`;
    } else if (data.type === "buttons") {
        data.content.forEach(button => {
            const btn = document.createElement("button");
            btn.textContent = button.label;
            btn.classList.add("quick-reply");
            btn.onclick = () => handleButtonClick(button.action);
            messageDiv.appendChild(btn);
        });
    } else if (data.type === "web_summary") {
        let summaryHTML = `<strong>🔍 Web Summary:</strong><p>${data.summary}</p>`;
        summaryHTML += `<div class="web-results">`;

        data.sources.forEach(src => {
            summaryHTML += `
                <div class="web-result" style="margin-bottom: 10px;">
                    <a href="${src.url}" target="_blank" style="font-weight: bold;">${src.title}</a><br>
                    <p style="margin: 5px 0;">${src.snippet}</p>
                </div>
            `;
        });

        summaryHTML += `</div>`;
        messageDiv.innerHTML = summaryHTML;
    } else {
        messageDiv.innerHTML = `<p>🤖 Unable to display this response format.</p>`;
    }

    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
}

    function scanImage() {
        const imageInput = document.getElementById("image_input");
        if (imageInput.files.length === 0) {
            appendMessage("❌ Please select an image to scan.", "error-message");
            return;
        }

        const formData = new FormData();
        formData.append("image", imageInput.files[0]);

        fetch("/scan_image", {
            method: "POST",
            body: formData
        })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    appendMessage("❌ " + data.error, "error-message");
                } else {
                    displayStructuredMessage(data);
                }
            })
            .catch(err => appendMessage("❌ Scan failed: " + err.message, "error-message"));
    }

function triggerWebSearch() {
    const input = document.getElementById("user_input");
    const query = input.value.trim();
    if (!query) return;

    const chatbox = document.getElementById("chatbox");
    const userMsg = document.createElement("p");
    userMsg.textContent = `🧑 You (web search): ${query}`;
    chatbox.appendChild(userMsg);

    fetch("/web_search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    })
        .then(res => res.json())
        .then(data => {
            displayStructuredMessage(data);
        })
        .catch(err => {
            console.error("Web search error:", err);
        });

    input.value = "";
}
