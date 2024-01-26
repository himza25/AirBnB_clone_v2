#!/usr/bin/python3
"""
This Flask web application provides two routes:
one for listing states and another for listing cities by states.
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


def sortdict(dictionary):
    """
    Sorts and returns a dictionary.
    """
    diction = {}
    for i in dictionary:
        diction[i] = dictionary[i]
    return diction


@app.route("/states_list", strict_slashes=False)
def states():
    """
    Route to display a list of states. Renders the states_list template.
    """
    return render_template('7-states_list.html', states=storage.all("State"))


@app.route("/cities_by_states", strict_slashes=False)
def cities_state():
    """
    Route to display a list of cities by states.
    Renders the cities_by_states template.
    """
    states = storage.all("State")
    cities_dict = {}
    for state in states.values():
        cities_dict[state.name] = sorted(
                                state.cities, key=lambda city: city.name
                                )
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities_dict)


@app.teardown_appcontext
def reset(error):
    """
    Clean-up method to close the storage connection after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
