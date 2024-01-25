#!/usr/bin/python3
"""
A Flask web application module.
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines a route '/' to display "Hello HBNB!".
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Route '/' to display 'Hello HBNB!' """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
