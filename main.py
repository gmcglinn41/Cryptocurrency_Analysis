#!/usr/bin/env python
# coding: utf-8

# In[2]:


#####
###
##
#    SYNOPSIS
#
#    Fill in later
#
#
#    CONTRIBUTORS
#    
#    Anna Dunnett https://github.com/adunnett
#    Connor Lane https://github.com/Move-7-8
#    Gail McGlinn https://github.com/gmcglinn41
#    John Bingley https://github.com/JB-DA
#
#    Source and output can be found (with access) on https://github.com/gmcglinn41/Cryptocurrency_Analysis
#
##
###
#####


### SETTINGS
##
# Dependencies
import pandas as pd
from sqlalchemy import create_engine
import requests
import json

#API KEY
coin_apikey1 = 'B44F0242-E0BA-4C1A-BED2-831A67426480'
coin_apikey = '1830D89F-A633-4F73-9707-3A7FAFE5C0F0'

### DOWNLOAD DATA FROM WEB API
##
#

## EXCHANGES
# https://rest.coinapi.io/v1/exchanges?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
url = 'https://rest.coinapi.io/v1/exchanges'
headers = { 'X-CoinAPI-Key' : coin_apikey }
response = requests.get(url, headers=headers)

with open( 'data_raw/exchanges.json', 'w' ) as ii:
    json.dump( response.json(), ii )

## ASSETS
# https://rest.coinapi.io/v1/assets?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
url = 'https://rest.coinapi.io/v1/assets'
headers = { 'X-CoinAPI-Key' : coin_apikey }
response = requests.get(url, headers=headers)

with open( 'data_raw/assets.json', 'w' ) as ii:
    json.dump( response.json(), ii )

## SYMBOLS
# https://rest.coinapi.io/v1/symbols?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
url = 'https://rest.coinapi.io/v1/symbols'
headers = { 'X-CoinAPI-Key' : coin_apikey }
response = requests.get(url, headers=headers)

with open( 'data_raw/symbols.json', 'w' ) as ii:
    json.dump( response.json(), ii )

## EXCHANGE-RATES
# https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = { 'X-CoinAPI-Key' : coin_apikey }
response = requests.get(url, headers=headers)

with open( 'data_raw/exchange_rates.json', 'w' ) as ii:
    json.dump( response.json(), ii )

## OHLCV - Open, High, Low, Close, Volume
# https://rest.coinapi.io/v1/ohlcv/periods?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
url = 'https://rest.coinapi.io/v1/ohlcv/periods'
headers = { 'X-CoinAPI-Key' : coin_apikey }
response = requests.get(url, headers=headers)

with open( 'data_raw/ohlcv.json', 'w' ) as ii:
    json.dump( response.json(), ii )

## ORDERBOOKS
# https://rest.coinapi.io/v1/orderbooks3/current?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
url = 'https://rest.coinapi.io/v1/orderbooks3/current'
headers = { 'X-CoinAPI-Key' : coin_apikey }
response = requests.get(url, headers=headers)

with open( 'data_raw/orderbooks.json', 'w' ) as ii:
    json.dump( response.json(), ii )


### API DATA LOAD & CLEAN
##
# Loads data file that was downloaded earlier using our API call

# exchanges.json
# assets.json
# symbols.json
# exchange_rates.json
# ohlcv.json
# orderbooks.json

with open( 'data_raw/exchanges.json', 'r' ) as jj: #open pre-downloaded api results
    json_d = json.load( jj )
    df_exchanges = pd.DataFrame( json_d ) #load to dataframe

with open( 'data_raw/assets.json', 'r' ) as jj: #open pre-downloaded api results
    json_d = json.load( jj )
    df_assets = pd.DataFrame( json_d ) #load to dataframe
    
with open( 'data_raw/symbols.json', 'r' ) as jj: #open pre-downloaded api results
    json_d = json.load( jj )
    df_symbols = pd.DataFrame( json_d ) #load to dataframe
    
with open( 'data_raw/exchange_rates.json', 'r' ) as jj: #open pre-downloaded api results
    json_d = json.load( jj )
    df_exchange_rates = pd.DataFrame( json_d ) #load to dataframe
    
with open( 'data_raw/ohlcv.json', 'r' ) as jj: #open pre-downloaded api results
    json_d = json.load( jj )
    df_ohlvc = pd.DataFrame( json_d ) #load to dataframe

with open( 'data_raw/orderbooks.json', 'r' ) as jj: #open pre-downloaded api results
    json_d = json.load( jj )
    df_orderbooks = pd.DataFrame( json_d ) #load to dataframe


### PUSH TO DATABASE
##
# Connect to database
engine = create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto_analysis_db")
engine.begin()
con = engine.connect()

# Check table names
engine.table_names()

# Load dataframes into database
df_exchanges.to_sql( name = 'themes', con = engine, if_exists = 'append', index = False )
df_assets.to_sql( name = 'sets', con = engine, if_exists = 'append', index = False )
df_sybmols.to_sql( name = 'inventories', con = engine, if_exists = 'append', index = False )
df_exchanges_rates.to_sql( name = 'inventory_sets', con = engine, if_exists = 'append', index = False )
df_ohlcv.to_sql( name = 'minifigs', con = engine, if_exists = 'append', index = False )
df_orderbooks.to_sql( name = 'inventory_minifigs', con = engine, if_exists = 'append', index = False )


# In[ ]:




