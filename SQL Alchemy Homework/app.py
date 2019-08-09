import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc
import datetime as dt
import numpy as np
engine = create_engine("sqlite:///hawaii.sqlite")
conn = engine.connect()

Base = automap_base()
Base.prepare(engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
from flask import Flask, jsonify, render_template
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.route("/")
def welcome():
   return (
       f"Welcome to the Hawaii Climate Analysis API!<br/>"
       f"Available Routes:<br/>"
       f"/api/v1.0/precipitation<br/>"
       f"/api/v1.0/stations<br/>"
       f"/api/v1.0/tobs<br/>"
       f"/api/v1.0/temp/start/end"
   )

@app.route("/api/v1.0/precipitation")
def precipitation():
	#last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
	first_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
# retrieve the last 12 months of precipitation data and plot the results
	one_year = session.query(Measurement.date, Measurement.prcp).\
                        filter(Measurement.date >= first_date).\
                        order_by(Measurement.date).all()
	precip = {date: prcp for date, prcp in one_year}
	return jsonify(precip)
	
	
@app.route("/api/v1.0/stations")
def stations():
	station_count = session.query(Station.station).all()
	stations = list(np.ravel(station_count))
	return jsonify(stations)

   
@app.route("/api/v1.0/tobs")
def tobs():
	temperatures_recorded = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs))\
	.filter(Measurement.station =='USC00519281').all()
	temps = list(np.ravel(temperatures_recorded))
	return jsonify(temps)
	
		
@app.route("/api/v1.0/temp/<start_date>/<end_date>")
def temp(start_date = None, end_date = None):
	start_end_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
	filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
	final_date = list(np.ravel(start_end_date))
	return jsonify(final_date)
	
if __name__ == '__main__':
	app.run(debug = True, port = 8000)