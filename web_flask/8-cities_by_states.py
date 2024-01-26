#!/usr/bin/python3
"""Start a Flask web application."""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of states and cities sorted by name."""
    states = storage.all("State").values()
    states_cities = {}
    for state in sorted(states, key=lambda s: s.name):
        states_cities[state] = sorted(state.cities, key=lambda c: c.name)
    return render_template('8-cities_by_states.html',
                           states_cities=states_cities)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
