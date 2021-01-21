import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from flask import Flask, jsonify, render_template, url_for, redirect 


#################################################
# Database Setup
#################################################
engine = create_engine(f"postgresql://postgres:fender2007@localhost:5433/crypto_analysis_db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():

    session = Session(engine)
    session.close()

    return render_template('index.html')

## ^^ Use HTML links to the other pages instead of the return of apis in routes (?)

@app.route("/api/overview")
def overview():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from asset_overview', dbConnect).head(20)
    overview_result = df.to_json(orient='records')
    dbConnect.close()
    return overview_result


@app.route("/api/symbols")
def symbols():

    dbConnect = engine.connect()
    df = pd.read_sql('select * from market_symbols', dbConnect).head(20)
    symbols_result = df.to_json(orient='records')
    dbConnect.close()
    return symbols_result

@app.route("/api/exchanges")
def exchange():

    dbConnect = engine.connect()
    df = pd.read_sql('select * from exchanges', dbConnect).head(20)
    exchange_result = df.to_json(orient='records')
    dbConnect.close()
    return exchange_result

@app.route("/api/historic_trades")
def historic():

    dbConnect = engine.connect()
    df = pd.read_sql('select * from historic_trades', dbConnect).head(20)
    historic_result = df.to_json(orient='records')
    dbConnect.close()
    return historic_result


if __name__ == '__main__':
    app.run(debug=True)
