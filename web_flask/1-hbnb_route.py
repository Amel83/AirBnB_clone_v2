#!/usr/bin/python3
"""to start flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print hbnb """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
