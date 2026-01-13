from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

viral_words = [
    "viral","trending","youtube","shorts","reels","2025",
    "best","new","latest","famous","popular","explore"
]

def make_tags(title):
    words = title.lower().split()
    tags = []
    for w in words:
        tags.append(w)
        tags.append(w + " video")
        tags.append("viral " + w)
    tags = list(set(tags + viral_words))
    return ", ".join(tags[:30])

def make_hashtags(title):
    words = title.lower().split()
    tags = ["#" + w.replace(" ","") for w in words]
    tags += ["#viral","#trending","#youtube","#shorts"]
    return " ".join(tags)

def make_description(title):
    desc = f"Watch {title}, this video is going viral on YouTube. Don't forget to like, share and subscribe."
    return desc + "\n\n" + make_hashtags(title)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    title = data["title"]
    tool = data["tool"]

    if tool == "tags":
        result = make_tags(title)
    elif tool == "hashtags":
        result = title + "\n" + make_hashtags(title)
    else:
        result = make_description(title)

    return jsonify({"result": result})

app.run(host="0.0.0.0", port=81)