import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from flask import Flask, jsonify, render_template, url_for, redirect 
import json
import jinja2

##### DATABASE SETUP
###
#
engine = create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto_analysis_db")
Base = automap_base()
Base.prepare(engine, reflect=True)

##### FLASK SETUP
###
#
app = Flask(__name__)

##### ROUTES
###
#

# API Pages
@app.route("/api/api_overview")
def api_overview():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from asset_overview', dbConnect).head(20)
    json_overview = json.loads(df.to_json(orient='records'))
    dbConnect.close()
    return jsonify(json_overview)

@app.route("/api/api_coins")
def api_coins():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from asset_overview', dbConnect).head(13)
    json_coins = json.loads(df.to_json(orient='records'))
    dbConnect.close()
    return jsonify(json_coins)

@app.route("/api/api_exchanges")
def api_exchanges():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from exchanges', dbConnect).head(20)
    json_exchanges = json.loads(df.to_json(orient='records'))
    dbConnect.close()
    return jsonify(json_exchanges)

@app.route("/api/api_historic")
def api_historic():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from historic_trades', dbConnect).head(20)
    json_historic = df.to_json(orient='records')
    dbConnect.close()
    return jsonify(json_historic)

# HTML PAGES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coins')
def coins():
    return render_template('coins.html')

@app.route('/exchanges')
def exchanges():
    return render_template('exchanges.html')

@app.route('/historic')
def historic():
    return render_template('historic.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/api')
def api():
    return render_template('api.html')

##### RUN THAT CODE
###
#
if __name__ == '__main__':
    app.run(debug=True)