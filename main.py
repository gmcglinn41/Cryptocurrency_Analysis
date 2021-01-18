#!/usr/bin/env python
# coding: utf-8


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
import psycopg2
import requests
import json

# API Keys
# Daily limits apply, make sure to only use 1
apikey_coinapi = 'B44F0242-E0BA-4C1A-BED2-831A67426480'
#apikey_coinapi = '1830D89F-A633-4F73-9707-3A7FAFE5C0F0'
#apikey_coinapi = '200EF4DD-8BF3-4A8A-9FC9-CF9C9D6D1173'


### EXTRACT, TRANSFORM, LOAD FUNCTIONS
##
# Individual functions to download, load, clean and push data to database

def api_download():
    
    # Exchanges
    # https://docs.coinapi.io/#list-all-exchanges
    url = 'https://rest.coinapi.io/v1/exchanges'
    headers = { 'X-CoinAPI-Key' : apikey_coinapi }
    response = requests.get(url, headers=headers)

    with open( 'data_raw/exchanges.json', 'w' ) as ii: #save api call to json file
        json.dump( response.json(), ii )

    # Assets
    # https://docs.coinapi.io/#list-all-assets
    url = 'https://rest.coinapi.io/v1/assets'
    headers = { 'X-CoinAPI-Key' : apikey_coinapi }
    response = requests.get(url, headers=headers)

    with open( 'data_raw/assets.json', 'w' ) as ii:
        json.dump( response.json(), ii )

    # Symbols
    # https://docs.coinapi.io/#list-all-symbols
    url = 'https://rest.coinapi.io/v1/symbols'
    headers = { 'X-CoinAPI-Key' : apikey_coinapi }
    response = requests.get(url, headers=headers)

    with open( 'data_raw/symbols.json', 'w' ) as ii:
        json.dump( response.json(), ii )

    # Exchange Rates
    # https://docs.coinapi.io/#exchange-rates
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = { 'X-CoinAPI-Key' : apikey_coinapi }
    response = requests.get(url, headers=headers)

    with open( 'data_raw/exchange_rates.json', 'w' ) as ii:
        json.dump( [response.json()], ii ) #add [] as file is not in proper format

    # OHLCV - Open, High, Low, Close, Volume
    # https://rest.coinapi.io/v1/ohlcv/periods?apikey=B44F0242-E0BA-4C1A-BED2-831A67426480
    url = 'https://rest.coinapi.io/v1/ohlcv/periods'
    headers = { 'X-CoinAPI-Key' : apikey_coinapi }
    response = requests.get(url, headers=headers)

    with open( 'data_raw/ohlcv.json', 'w' ) as ii:
        json.dump( response.json(), ii )

    # Orderbooks
    # https://docs.coinapi.io/#order-book-l3
    
    ### DOWNLOAD DATA FROM WEB API'S
    ##
    #
    
#END api_download


def api_dataframe_load():
    
    with open( 'data_raw/exchanges.json', 'r' ) as jj: #open api results
        json_d = json.load( jj )
        global df_exchanges 
        df_exchanges = pd.DataFrame( json_d ) #save to dataframe

    with open( 'data_raw/assets.json', 'r' ) as jj:
        json_d = json.load( jj )
        global df_assets
        df_assets = pd.DataFrame( json_d )

    with open( 'data_raw/symbols.json', 'r' ) as jj:
        json_d = json.load( jj )
        global df_symbols
        df_symbols = pd.DataFrame( json_d )

    with open( 'data_raw/exchange_rates.json', 'r' ) as jj:
        json_d = json.load( jj )
        global df_exchange_rates
        df_exchange_rates = pd.DataFrame( json_d )

    with open( 'data_raw/ohlcv.json', 'r' ) as jj:
        json_d = json.load( jj )
        global df_ohlcv
        df_ohlcv = pd.DataFrame( json_d )
    
    ### API DATA LOAD
    ##
    # Loads data file that was downloaded using API calls, stores into dataframe object
    
#END api_dataframe_load


def dataframe_clean():
    
    global df_transform_exchanges
    global df_transform_assets
    global df_transform_symbols
    
    df_transform_exchanges = df_exchanges[[ 'exchange_id', 'website', 'name', 'data_symbols_count', 'volume_1mth_usd' ]]
    df_transform_assets = df_assets[[ 'asset_id', 'name', 'price_usd' ]]
    df_transform_symbols = df_symbols[[ 'symbol_id', 'exchange_id', 'asset_id_base', 'asset_id_quote' ]]
    #df_transform_exchange_rates
    #df_transform_ohlcv
    
    ### DATAFRAME CLEAN
    ##
    # Cleans data files to contain only required information in dataframe object
    
#END dataframe_clean


def database_push():

    # Connect to database
    engine = create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto_analysis_db")
    engine.begin()
    con = engine.connect()

    # Check table names
    engine.table_names()

    # Load dataframes into database
    
    df_transform_exchanges.to_sql( name = 'exchanges', con = engine, if_exists = 'append', index = False )
    df_transform_assets.to_sql( name = 'assets', con = engine, if_exists = 'append', index = False )
    df_transform_symbols.to_sql( name = 'symbols', con = engine, if_exists = 'append', index = False )
#    df_exchanges_rates.to_sql( name = 'inventory_sets', con = engine, if_exists = 'append', index = False )
#    df_ohlcv.to_sql( name = 'minifigs', con = engine, if_exists = 'append', index = False )
    
    con.close()
    engine.dispose()
    
    ### PUSH TO DATABASE
    ##
    # Connect to postgresql database and export cleaned dataframe objects
    
#END database_push


def dataframe_display():

#     display( df_exchanges )
#     display( df_assets )
#     display( df_symbols )
#     display( df_exchange_rates )
#     display( df_ohlcv )
    
    display( df_transform_exchanges )
    display( df_transform_assets )
    display( df_transform_symbols )
    
    ### DISPLAY DATAFRAMES TO CHECK DATA
    ##
    # Used to check correct downloading of API, datarame loading and cleaning
    
#END dataframe_display


### FUNCTION CALLS
##
# Don't need to run all of these, just that which needs to be updated

#api_download()
api_dataframe_load()
dataframe_clean()
database_push()
#dataframe_display()

