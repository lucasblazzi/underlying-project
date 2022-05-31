import os
import json
import hashlib

import numpy as np
import pandas as pd
from option import OptionCall, OptionPut

base_path = os.path.dirname(os.path.abspath(__file__))

underlying_cols = ["name_underlying", "company_underlying", "close_price_underlying"]


class Builder:
    def __init__(self, dfs, year):
        self.dfs = dfs
        self.names = json.load(open(os.path.join(base_path, "./plans/names.json"), encoding="utf8"))
        self.year = year

    @property
    def architect(self):
        results = list()
        if isinstance(self.dfs, list):
            result = pd.concat([self.build(df) for df in self.dfs])
        else:
            result = self.build(self.dfs)

        underlyings = result[(result["folder"] == "acoes")]
        options = result[(result["folder"] == "opcoes")]
        # sample_options = options[options["name"].str.contains("BOV|VAL|PET")==True]
        for k, raw_df in options.groupby(["name", "folder", "type", "exercise_price", "expiration_date", "isin_code"]):
            print(k[0])
            hash_obj = k + (str(self.year), )
            group_hash = hashlib.md5(str(hash_obj).encode()).hexdigest()
            raw_df["id"] = group_hash
            df = pd.merge(raw_df, underlyings, how="left", on=["isin_code", "date"], suffixes=("", "_underlying"))
            df = df[raw_df.columns.tolist() + underlying_cols]
            df["expiration_time"] = (df["expiration_date"] - df["date"]).dt.days / 365
            df["return_underlying"] = df["close_price_underlying"].pct_change().fillna(0)
            df = self.calculate(df)
            df["date"] = df["date"].dt.strftime('%Y-%m-%d')
            df["expiration_date"] = df["expiration_date"].dt.strftime('%Y-%m-%d')
            df.index.name = f"name={k[0]}/{group_hash}"
            results.append(df)
        return results

    @staticmethod
    def calculate(df, periods_in_year: int = 252):
        df["volatility_underlying"] = df["return_underlying"].std(ddof=1) * np.sqrt(periods_in_year)
        option_type = df["type"].iloc[-1]
        if option_type == "CALL":
            df = OptionCall(df).features
        elif option_type == "PUT":
            df = OptionPut(df).features
        else:
            print("UNIDENTIFIED OPTION TYPE")
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.fillna(0)
        return df

    def market_view(self, market):
        if market in self.names["derivative_types"]:
            return "derivatives"
        return "stocks"

    @staticmethod
    def piper(name):
        _pipes = {
            "cotahist": "daily_data",
            "tradeintraday": "intra_day_data",
        }
        return _pipes.get(name)

    def build(self, df):
        name = df.index.name
        piper = self.piper(name)
        col_names = self.names[piper]
        if isinstance(col_names, list):
            df.columns = col_names
        else:
            df = df.rename(columns=col_names)
        return df.pipe(getattr(self, piper))

    def map_bdi(self, bid):
        return self.names["bdi_code_mapper"][str(int(bid))]

    def map_market(self, market):
        return self.names["market_type_mapper"][str(int(market))]

    def map_folder(self, market_type):
        return self.names["folder_mapper"][market_type]

    def map_type(self, market_type):
        return self.names["option_type_mapper"].get(market_type, "")

    @staticmethod
    def parse_date(date_input):
        date = date_input.split(".")[0]
        return f"{date[0:4]}-{date[4:6]}-{date[6:8]}"

    def daily_data(self, df):
        cols_to_drop = ["market_type", "bdi_code"]
        df = df.drop(df.shape[0] - 1)
        for column in self.names["daily_comma_parse"]:
            df[column] = df[column]/100
        df["date"] = pd.to_datetime(df["date"].apply(lambda x: self.parse_date(str(x))))
        df["expiration_date"] = pd.to_datetime(df["expiration_date"].apply(
            lambda x: self.parse_date(str(x))), errors="coerce")
        df["bdi_code"] = df["bdi_code"].apply(lambda x: self.map_bdi(x))
        df["market_type"] = df["market_type"].apply(lambda x: self.map_market(x))
        df["type"] = df["market_type"].apply(lambda x: self.map_type(x))
        df["folder"] = df["market_type"].apply(lambda x: self.map_folder(x))
        df = df.drop(columns=cols_to_drop)
        return df
