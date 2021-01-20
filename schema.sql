-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Exchanges" (
    "exchange_id" VARCHAR   NOT NULL,
    "website" VARCHAR   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "data_symbols_count" VARCHAR   NOT NULL,
    "volume_1mth_usd" FLOAT   NOT NULL,
    CONSTRAINT "pk_Exchanges" PRIMARY KEY (
        "exchange_id"
     )
);

CREATE TABLE "Market_Symbols" (
    "symbol_id" VARCHAR   NOT NULL,
    "exchange_id" VARCHAR   NOT NULL,
    "asset_id_base" VARCHAR   NOT NULL,
    "asset_id_quote" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Market_Symbols" PRIMARY KEY (
        "symbol_id"
     )
);

CREATE TABLE "Asset_Overview" (
    "asset_id" VARCHAR   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "price_usd" FLOAT   NOT NULL,
    CONSTRAINT "pk_Asset_Overview" PRIMARY KEY (
        "asset_id"
     )
);

CREATE TABLE "Historic_Trades" (
    "symbol_id" VARCHAR   NOT NULL,
    "price" int   NOT NULL,
    "size" int   NOT NULL,
    CONSTRAINT "pk_Historic_Trades" PRIMARY KEY (
        "symbol_id"
     )
);

ALTER TABLE "Market_Symbols" ADD CONSTRAINT "fk_Market_Symbols_exchange_id" FOREIGN KEY("exchange_id")
REFERENCES "Exchanges" ("exchange_id");

ALTER TABLE "Market_Symbols" ADD CONSTRAINT "fk_Market_Symbols_asset_id_base" FOREIGN KEY("asset_id_base")
REFERENCES "Asset_Overview" ("asset_id");

ALTER TABLE "Historic_Trades" ADD CONSTRAINT "fk_Historic_Trades_symbol_id" FOREIGN KEY("symbol_id")
REFERENCES "Market_Symbols" ("symbol_id");

