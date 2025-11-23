import os
import requests
from flask import Flask, request

TOKEN = "8202432812:AAF7PWDOYl-cN0FSaBsRKAeo6XiD2DOGP98"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

# Webhook endpoint
@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id,
                         "Hello! 👋\nYour auto-order bot is running successfully!")

        else:
            send_message(chat_id, f"You said: {text}")

    return "OK", 200


def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


@app.route("/setwebhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://rici-autoorder-bot.onrender.com"
    url = f"{BASE_URL}/setWebhook?url={webhook_url}"
    response = requests.get(url)
    return response.json()


@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
