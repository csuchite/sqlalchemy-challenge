 #1. import Flask
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

engine = create_engine('sqlite:///hawaii.sqlite', echo=False)

# Declare a Base using `automap_base()`
Base = automap_base()

# Reflect Database into ORM classes
Base.prepare(engine, reflect=True)

# Save a reference to the measurenment table as 'Measurement'
Measurement = Base.classes.measurement
# Save a reference to the station table as 'Station'
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    """List of available routes."""

    return (
        "Hawaii Precipitation and Weather data<br/><br/>"
        "Pick from the available routes below:<br/><br/>"
        "Precipiation from 2016-08-23 to 2017-08-23.<br/>"
        "/api/v1.0/precipitation<br/><br/>"
        "A list of all the weather stations in Hawaii.<br/>"
        "/api/v1.0/stations<br/><br/>"


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def PRCP():
     """Query for the dates and temperature observations from the last year.
    Convert the query results to a Dictionary using date as the 'key 'and 'tobs' as the value."""
# The last 12 months  
   results = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date > begin.date).\
            order_by(Measurement.date).all()

prcp_data =[]
for prcp_data in results:
    prcp_data ={}
    prcp_data_dict["Data"] = prcp_data.date
    prcp_data_dict["Precipitation"] = prcp_data.prcp
    precipitation_data.append(prcp_data_dict)


return jsonify(precipitation_data)



@app.route("/api/v1.0/stations")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/tobs")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"




if __name__ == "__main__":
    app.run(debug=True)
