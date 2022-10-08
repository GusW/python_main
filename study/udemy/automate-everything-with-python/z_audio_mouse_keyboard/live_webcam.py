from cv2 import VideoCapture, imencode
from flask import Flask, render_template, Response

from z_audio_mouse_keyboard.constants import INDEX_HTML_NAME

video = VideoCapture(0)  # int 0: main device camera; 1, 2...


def generate_frames():
    while True:
        _, frame = video.read()
        _, encoded_image = imencode(".jpg", frame)
        new_frame = encoded_image.tobytes()
        yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + new_frame + b"\r\n")


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(INDEX_HTML_NAME)


@app.route("/video_feed_url")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


def main():
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
