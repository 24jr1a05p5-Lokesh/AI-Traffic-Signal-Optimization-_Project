from flask import Flask, render_template, request
import os
from detect import detect_traffic

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    video = request.files["video"]

    filename = "traffic.mp4.mp4"

    if not os.path.exists("videos"):
        os.makedirs("videos")

    video_path = os.path.join("videos", filename)

    video.save(video_path)

    result = detect_traffic()

    return render_template(
        "result.html",
        **result
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)