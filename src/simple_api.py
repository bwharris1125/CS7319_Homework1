"""This is a simple Flask API to support CS7319 Homework 1."""

from flask import Flask

app = Flask(__name__)
port = 5000

@app.route("/")
def hello_world():
    """Return a HTTP greeting when localhost:<port> is visted."""
    return "Hello, World!"


@app.route("/welcome")
def welcome():
    """Return a welcome message."""
    return "Welcome to CS 7319!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=False)
