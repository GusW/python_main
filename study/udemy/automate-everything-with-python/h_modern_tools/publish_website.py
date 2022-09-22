"""
https://replit.com/@gusw/repltestdrive#main.py
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Nothing for you here, punk."


if __name__ == "__main__":
    app.run(host="0.0.0.0")
