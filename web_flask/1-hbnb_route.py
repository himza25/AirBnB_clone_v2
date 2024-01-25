#!/usr/bin/python3
"""
A Flask web application module.
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines routes '/' and '/hbnb'.
'/' route displays "Hello HBNB!" and '/hbnb' route displays "HBNB".
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Route '/' to display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Route '/hbnb' to display 'HBNB' """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
