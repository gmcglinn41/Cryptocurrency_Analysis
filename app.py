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

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

##### FLASK SETUP
###
#
app = Flask(__name__)

##### ROUTES
###
#

# API Pages
@app.route("/api/overview")
def overview():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from asset_overview', dbConnect).head(20)
    results = df.to_json(orient='records')
    json_overview = json.loads(results)
    #json.dumps(parsed)
    dbConnect.close()
    return jsonify(json_overview)

    # dump_data = dumps(data)
    # json_data = json.loads(dump_data)
    # return jsonify(json_data) 
    # dump_latest = dumps(latest) 
    # json_latest = json.loads(dump_latest)
    # return jsonify(json_latest)

# @app.route("/api/")
# def index():
#     dbConnect = engine.connect()
#     df = pd.read_sql('select * from asset_overview', dbConnect).head(20)
#     results_index = df.to_json(orient='records')
#     dbConnect.close()
#     return (results_index)

# @app.route("/api/overview")
# def index():
#     dbConnect = engine.connect()
#     df = pd.read_sql('select * from asset_overview', dbConnect).head(20)
#     results_index = df.to_json(orient='records')
#     dbConnect.close()
#     return (results_index)

# @app.route("/api/overview")
# def index():
#     dbConnect = engine.connect()
#     df = pd.read_sql('select * from asset_overview', dbConnect).head(20)
#     results_index = df.to_json(orient='records')
#     dbConnect.close()
#     return (results_index)

# HTML PAGES
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/coins')
# def coins():
#     return render_template('coins.html')

# @app.route('/markets')
# def markets():
#     return render_template('markets.html')

# @app.route('/data')
# def data():
#     return render_template('data.html')

# @app.route('/team')
# def team():
#     return render_template('team.html')

# @app.route('/api')
# def api():
#     return render_template('api.html')

##### RUN THAT CODE
###
#
if __name__ == '__main__':
    app.run(debug=True)