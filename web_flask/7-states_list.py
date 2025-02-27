#!/usr/bin/python3
"""Start a Flask web application."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all states sorted by name."""
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
