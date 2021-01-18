import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, url_for, redirect 


#################################################
# Database Setup
#################################################
engine = create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto_analysis_db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
# Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def overview():

    session = Session(engine)
    session.close()

    return render_template('overview.html', overview=overview)
## Use HTML links to the other pages instead of the return of apis in routes


@app.route("/api/v1.0/changes")
def change():

    session = Session(engine)
    session.close()

    return render_template('change.html', pricechange=pricechange)


@app.route("/api/v1.0/coin_family")
def coinfamily():

    session = Session(engine)
    session.close()

    return render_template('change.html', pricechange=pricechange)


@app.route("/api/v1.0/overview")
def names():

    session = Session(engine)
    session.close()  

    return render_template('change.html', pricechange=pricechange)


if __name__ == '__main__':
    app.run(debug=True)
