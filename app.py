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
table_overview = Base.classes.asset_overview
#table_market_symbols = Base.classes.market_symbols
#table_exchanges = Base.classes.exchanges
#table_historic_trades = Base.classes.historic_trades

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
    #Uses the asset overview table
    asset_id = session.query(table_overview.asset_id).all()
    name = session.query(table_overview.name).all()
    price_usd = session.query(table_overview.price_usd).all()

    session.close()

    return render_template('index.html', asset_id=asset_id)
## Use HTML links to the other pages instead of the return of apis in routes


# @app.route("/api/v1.0/changes")
# def change():

#     session = Session(engine)

#     historic_trades = session.query(table_historic_trades).all()
#     # price = session.query(table_historic_trades.price).all()
#     # size = session.query(table_historic_trades.size).all()

#     session.close()

#     return jsonify(historic_trades)
#     # render_template('changes.html', change=change)

# @app.route("/api/v1.0/exchanges")
# def exchange():

#     session = Session(engine)

#     exchange_id = session.query(table_exchanges).all()
#     website = session.query(table_exchanges).all()
#     name = session.query(table_exchanges).all()
#     data_symbols_count = session.query(table_exchanges).all()
#     volume_1mth_usd = session.query(table_exchanges).all()

#     session.close()  

#     return render_template('exchanges.html', exchange=exchange)


# ## Only doing coin family if we have time 

# # @app.route("/api/v1.0/coin_family")
# # def coinfamily():

# #     session = Session(engine)



# #     session.close()

# #     return render_template('coin_family.html', coin_fam=coin_fam)


if __name__ == '__main__':
    app.run(debug=True)
