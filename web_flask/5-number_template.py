#!/usr/bin/python3
"""Run Flask server."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return greeting message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Return 'C ' followed by the formatted text."""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text="is cool"):
    """Return 'Python ' followed by the formatted text."""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def integer(n):
    """Return string confirming n is a number."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def integer_template(n):
    """Render HTML template if n is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
