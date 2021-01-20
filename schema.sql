-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "exchanges" (
    "exchange_id" VARCHAR   NOT NULL,
    "website" VARCHAR   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "data_symbols_count" VARCHAR   NOT NULL,
    "volume_1mth_usd" FLOAT   NOT NULL,
    CONSTRAINT "pk_exchanges" PRIMARY KEY (
        "exchange_id"
     )
);

CREATE TABLE "market_symbols" (
    "symbol_id" VARCHAR   NOT NULL,
    "exchange_id" VARCHAR   NOT NULL,
    "asset_id_base" VARCHAR   NOT NULL,
    "asset_id_quote" VARCHAR   NOT NULL,
    CONSTRAINT "pk_market_symbols" PRIMARY KEY (
        "symbol_id"
     )
);

CREATE TABLE "asset_overview" (
    "asset_id" VARCHAR   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "price_usd" FLOAT   NOT NULL,
    CONSTRAINT "pk_asset_overview" PRIMARY KEY (
        "asset_id"
     )
);

CREATE TABLE "historic_trades" (
    "symbol_id" VARCHAR   NOT NULL,
    "price" int   NOT NULL,
    "size" int   NOT NULL,
    CONSTRAINT "pk_historic_trades" PRIMARY KEY (
        "symbol_id"
     )
);

ALTER TABLE "market_symbols" ADD CONSTRAINT "fk_market_symbols_exchange_id" FOREIGN KEY("exchange_id")
REFERENCES "exchanges" ("exchange_id");

ALTER TABLE "market_symbols" ADD CONSTRAINT "fk_market_symbols_asset_id_base" FOREIGN KEY("asset_id_base")
REFERENCES "asset_overview" ("asset_id");

ALTER TABLE "historic_trades" ADD CONSTRAINT "fk_historic_trades_symbol_id" FOREIGN KEY("symbol_id")
REFERENCES "market_symbols" ("symbol_id");

