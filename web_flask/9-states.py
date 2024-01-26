#!/usr/bin/python3
"""
This module starts a Flask web application to display states and cities.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ Display a HTML page with a list of all states. """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, state_id=None)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """ Display a HTML page with cities of a specific state. """
    states = storage.all(State)
    state = None
    # Check if state with the given id exists
    for st in states.values():
        if st.id == id:
            state = st
            break
    return render_template('9-states.html', state=state, state_id=id)


@app.teardown_appcontext
def close_session(exception):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
