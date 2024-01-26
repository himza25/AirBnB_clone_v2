#!/usr/bin/python3
"""
Flask web application that displays cities by states from the storage engine.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Renders a HTML page listing all States and their Cities.
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """
    Closes the SQLAlchemy session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
