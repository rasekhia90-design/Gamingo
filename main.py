import requests
from flask import Flask, request

TOKEN = 479360511:U1r20jWEbJSP6nrMRp82G57FndnzmayUprk

app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    })

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        user_id = data["message"]["from"]["id"]

        send_message(user_id, f"🆔 آیدی شما:\n{user_id}")

    return "ok"

if __name__ == "__main__":
    app.run()
