#!/usr/bin/python3
"""
    Module implementing a script that starts web application
    with serveral routes defined

"""
from flask import Flask


app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello():
    """function defining home route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function defining route to hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
