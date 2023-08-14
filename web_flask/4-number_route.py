#!/usr/bin/python3
"""
    Script that start a flask application
    and check is it a number passed in URL
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    return "hello HBNB!"


@app.route("/hbnb")
def display_hbnb():
    return "HBNB"


@app.route("/c/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/c/<text>")
def display_text_c(text):
    text = escape(text.replace("_", " "))
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def display_python(text):
    text = escape(text.replace("_", " "))
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_number(n):
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
