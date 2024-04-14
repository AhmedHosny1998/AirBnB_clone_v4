#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
import uuid
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ close the session sqlalchemy"""
    storage.close()

@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ hbnb"""
    cash_id = str(uuid.uuid4())
    state = storage.all(State).values()
    state = sorted(state, key = lambda k: k.name)
    st_ct = []


    for state in states:
        st_ct.append(state, sorted(state.cities, key=lambda k: k.name))

    amenities = storage.all(Amenities).values()
    amenities = sorted(amenities, key = lambda k: k.name)


    places = storage.all(places).values()
    places = sorted(places, key = lambda k: k.name )

    return render_template('0-hbnb.html','states=st_ct','places=places','cash_id=cash_id')



if __name__ == "__main__":
    """main"""
    app.run(host = '0.0.0.0', port = 5000)
    
