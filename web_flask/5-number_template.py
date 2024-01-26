#!/usr/bin/python3
"""
A Flask web application module.
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines routes '/', '/hbnb', '/c/<text>', '/python/(<text>)', '/number/<n>',
and '/number_template/<n>'.
'/' route displays "Hello HBNB!", '/hbnb' route displays "HBNB",
'/c/<text>' displays "C " followed by the value of the text variable,
'/python/(<text>)' displays "Python ",
followed by the value of the text variable.
'/number/<n>' displays "n is a number" only if n is an integer,
'/number_template/<n>' renders an HTML template only if n is an integer.
"""

from flask import Flask, render_template
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
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Renders an HTML template only if n is an integer. """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
