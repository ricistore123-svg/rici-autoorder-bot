from flask import Flask, request
import requests
import os

TOKEN = "8202432812:AAF7PWDOYl-cN0FSaBsRKAeo6XiD2DOGP98"
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", json={"chat_id": chat_id, "text": text})

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        data = request.get_json()
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text")

        send_message(chat_id, "Order received ✔️\nWe will process it soon.")
        return "OK"
    else:
        return "Hello from bot!"

if __name__ == "__main__":
    app.run()
