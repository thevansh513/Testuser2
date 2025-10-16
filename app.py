from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://biggestsmmpanel.com/api/v2"
API_KEY = os.environ.get("API_KEY")  # Render environment variable
SERVICE_ID = 4824

def order_video(video_link, quantity):
    payload = {
        "key": API_KEY,
        "action": "add",
        "service": SERVICE_ID,
        "link": video_link,
        "quantity": quantity
    }

    response = requests.post(API_URL, data=payload)
    return response.json()

@app.route("/order", methods=["GET"])
def place_order():
    video_link = request.args.get("video")
    quantity = request.args.get("qty")

    if not video_link or not quantity:
        return jsonify({"error": "Missing parameters: use /order?video=<link>&qty=<number>"}), 400

    try:
        quantity = int(quantity)
    except:
        return jsonify({"error": "Quantity must be a number"}), 400

    result = order_video(video_link, quantity)
    return jsonify(result)

@app.route("/")
def home():
    return "✅ SMM Panel Order Bot is running! Use /order?video=<link>&qty=<number>"
