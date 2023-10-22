#!/usr/bin/python3
"""start flask web app"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """char C then the value of text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Print Python, then value of text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ number route """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
