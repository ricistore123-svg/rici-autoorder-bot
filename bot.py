from flask import Flask, request
import requests
import os

BOT_TOKEN = "8202432812:AAF7PWDOYl-cN0FSaBsRKAeo6XiD2DOGP98"
WEBHOOK_URL = "https://rici-autoorder-bot.onrender.com/webhook"

app = Flask(__name__)

# --- Set webhook automatically on startup ---
def set_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}"
    r = requests.get(url)
    print("Webhook set:", r.text)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # simple reply
        send_message(chat_id, "Hello! Bot working ✅")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    set_webhook()
    app.run(host="0.0.0.0", port=10000)
