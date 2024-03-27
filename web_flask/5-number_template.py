#!/usr/bin/python3
"""
    Module implementing a script that starts a web application with
    defined routes

"""
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


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
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """function defining python route"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function defining number route"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """function defining number_template route"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
