#!/usr/bin/python3
"""the 1st question """
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """to print it"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
