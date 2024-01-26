#!/usr/bin/python3
"""
Flask web application that displays states and cities.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Displays a HTML page listing all States.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('9-states.html', states=sorted_states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page for a specific State and its Cities.
    """
    states = storage.all(State).values()
    state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', state=state, id=id)


@app.teardown_appcontext
def close_session(exception):
    """
    Closes the SQLAlchemy session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
