#!/usr/bin/python3
"""
This module starts a Flask web application with dynamic filters.
"""

from flask import Flask, render_template
from models import storage, State, City, Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Display a HTML page with dynamic filters. """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(exception):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
