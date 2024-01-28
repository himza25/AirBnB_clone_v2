#!/usr/bin/python3
"""
This module starts a Flask web application with dynamic content for HBNB.
"""

from flask import Flask, render_template
from models import storage, State, City, Amenity, Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Render the HBNB page with states, cities, amenities, and places. """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_session(exception):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
