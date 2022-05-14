import os
import json
import hashlib

import pandas as pd

base_path = os.path.dirname(os.path.abspath(__file__))


class Builder:
    def __init__(self, dfs):
        self.dfs = dfs
        self.names = json.load(open(os.path.join(base_path, "./plans/names.json"), encoding="utf8"))

    @property
    def architect(self):
        if isinstance(self.dfs, list):
            result = pd.concat([self.build(df) for df in self.dfs])
        else:
            result = self.build(self.dfs)

        results = list()
        for k, df in result.groupby(["name", "folder", "market_type", "exercise_price", "expiration_date", "isin_code"]):
            if k[1] == "opcoes":
                group_hash = hashlib.md5(str(k).encode()).hexdigest()
                df["id"] = group_hash
                df.index.name = f"name={k[0]}/{group_hash}"
                results.append(df)
        return results

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

    @staticmethod
    def parse_date(date_input):
        date = date_input.split(".")[0]
        return f"{date[0:4]}-{date[4:6]}-{date[6:8]}"

    def daily_data(self, df):
        df = df.drop(df.shape[0] - 1)
        for column in self.names["daily_comma_parse"]:
            df[column] = df[column]/100
        df["date"] = pd.to_datetime(df["date"].apply(lambda x: self.parse_date(str(x))))
        df["expiration_date"] = pd.to_datetime(df["expiration_date"].apply(
            lambda x: self.parse_date(str(x))), errors="coerce")
        df["bdi_code"] = df["bdi_code"].apply(lambda x: self.map_bdi(x))
        df["market_type"] = df["market_type"].apply(lambda x: self.map_market(x))
        df["folder"] = df["market_type"].apply(lambda x: self.map_folder(x))
        return df
