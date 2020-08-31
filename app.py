
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
measurement = Base.classes.measurement
station = Base.classes.station

# 1. Import Flask
from flask import Flask, jsonify

# 2. Create an app
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>Stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>Temp_observed</a><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date > '2016-08-23').\
    order_by(measurement.date).all()
    session.close()
    all_results = list(np.ravel(results))
    return jsonify(all_results)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    most_act_station = session.query(measurement.station, func.count(measurement.station)).\
    group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    session.close()
    all_results = list(np.ravel(most_act_station))
    return jsonify(all_results)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    highesttemp_perstation = session.query(measurement.station, func.max(measurement.tobs)).\
    group_by(measurement.station).order_by(func.max(measurement.tobs).desc()).all()
    session.close()
    all_results = list(np.ravel(highesttemp_perstation))
    return jsonify(all_results)




# 5. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
