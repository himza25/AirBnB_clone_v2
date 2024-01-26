#!/usr/bin/python3
"""
A Flask web application module.
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines routes '/', '/hbnb', '/c/<text>', and '/python/(<text>)'.
'/' route displays "Hello HBNB!", '/hbnb' route displays "HBNB",
'/c/<text>' displays "C " followed by the value of the text variable, and
'/python/(<text>)' displays "Python ", followed by the value.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ Displays 'Python ' followed by the value of the text variable. """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
