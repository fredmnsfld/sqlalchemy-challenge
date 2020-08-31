%matplotlib inline
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

# 2.1 Global Variable
hello_dict = [{"Hello": "World!"},{"Hello":"Portland!"}]

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>Precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>Stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>Temp_observed</a><br/>"
        f"<a href='/api/v1.0/countryitemtotals/USA'>countryitemtotals/USA</a><br/>"
        f"<a href='/api/v1.0/postcodeitemtotals/USA'>postcodeitemtotals/USA</a><br/>"
    )

# 3. Define static routes
@app.route("/")
def index():
    return "Hello, world!"


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()
    session.close()
    all_results = list(np.ravel(results))
    return jsonify(all_results)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()
    session.close()
    all_results = list(np.ravel(results))
    return jsonify(all_results)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()
    session.close()
    all_results = list(np.ravel(results))
    return jsonify(all_results)


@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)    

# 4. define jsonified route
@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


# 5. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
