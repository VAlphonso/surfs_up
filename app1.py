# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello World. It's really nice to meet you."

# if __name__ == "__main__":
#     app.run(debug=True)

# Add dependencies
import datetime as dt
import numpy as no
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# SET UP DATABASE

# Access SQLite database
engine = create_engine('sqlite:///hawaii.sqlite')

# Reflect the database into our classes
Base = automap_base()

# Reflect the tables of our database
Base.prepare(engine, reflect=True)

# Create variables for each class to reference laer
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# SET UP FLASK

# Create Flask application called "app"
app = Flask(__name__)

@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')