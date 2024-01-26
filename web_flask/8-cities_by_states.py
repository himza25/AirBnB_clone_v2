#!/usr/bin/python3
"""Start web application to display cities by states."""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Render template with states and their cities, sorted alphabetically.
    """
    states = storage.all(State)
    # Sort State objects alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
    Clean-up session.
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
