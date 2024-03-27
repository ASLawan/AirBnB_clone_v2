#!/usr/bin/python3
"""
    Modeule implementing a script that defines given routes and
    renders text to templates

"""
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")
app.config['STRICT_SLASHES'] = False


@app.route('/')
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """returns formatted string"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """returns formatted string"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>')
def number(n):
    """returns an integer"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """renders integers to a template"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """renders integers with odd or even status"""
    e = render_template('6-number_odd_or_even.html', number=n, status='even')
    o = render_template('6-number_odd_or_even.html', number=n, status='odd')
    if isinstance(n, int):
        if n % 2 == 0:
            return e
        else:
            return o


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
