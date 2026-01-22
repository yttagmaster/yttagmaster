import requests
import json

def youtube_raw_data(query):
    url = "https://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "ds": "yt",
        "q": query
    }
    r = requests.get(url, params=params)
    data = json.loads(r.text)
    return data[1]   # यही असली tags हैं

print(youtube_raw_data("ram navami"))
from flask import Flask, request, jsonify
import requests, json

app = Flask(__name__)

def youtube_raw_data(query):
    url = "https://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "ds": "yt",
        "q": query
    }
    r = requests.get(url, params=params)
    data = json.loads(r.text)
    return data[1]

@app.route("/api")
def api():
    q = request.args.get("q")
    data = youtube_raw_data(q)
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)
