#!/usr/bin/python3
"""
    Script that starts a flask application with argument after slash
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    text = escape(text.replace("_", " "))
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
