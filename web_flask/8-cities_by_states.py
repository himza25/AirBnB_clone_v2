#!/usr/bin/python3
"""
Flask web application that displays cities by states from the storage engine.
"""

from flask import Flask, render_template
from models import storage
from models.state import State  # Importing State if it's not already imported in models

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Renders a HTML page listing all States and their Cities, sorted alphabetically.
    """
    states = storage.all(State).values()
    cities_dict = {}
    for state in states:
        cities_dict[state.name] = sorted(state.cities, key=lambda city: city.name)
    # Sort states alphabetically by name
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states, cities=cities_dict)

@app.teardown_appcontext
def close_session(exception):
    """
    Closes the SQLAlchemy session after each request.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
