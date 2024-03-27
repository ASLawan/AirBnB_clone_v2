#!/usr/bin/python3
"""
    Module implementing a script that starts a flask web application
    with given routes

"""
from flask import Flask
from urllib.parse import unquote


app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello():
    """function defining home route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function defining hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """function defining c route"""
    text = unquote(text.replace('_', ' '))
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """function defining python route"""
    text = unquote(text.replace('_', ' '))
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function defining number route"""
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
