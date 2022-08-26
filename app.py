import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine,reflect=True)

Measurement = Base.classes.measurement

Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available API routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date,Measurement.prcp)

    session.close()


    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        prcp_data.append(prcp_dict)
    print(prcp_dict)


    return jsonify(prcp_data)



if __name__ == "__main__":
    app.run(debug=True)