

class OptionBuilder:
    def __init__(self, df, option, payoff):
        self.df = df
        self.option = option
        self.payoff = payoff
        self.result = dict()

    @property
    def build(self):
        self.build_base_info()
        self.build_greeks()
        self.build_market()
        self.build_price()
        self.build_option_close_series()
        self.build_payoff()
        return self.result

    def build_base_info(self):
        base_cols = ["id", "name", "type", "exercise_price", "currency", "expiration_date",
                     "name_underlying", "expiration_time"]
        self.result = {col: self.option[col] for col in base_cols}

    def build_greeks(self):
        greek_cols = ["gamma", "delta", "theta", "rho", "gamma", "vega"]
        self.result["greeks"] = [{"name": greek, "value": self.option[greek]} for greek in greek_cols]

    def build_market(self):
        market_cols = ["option_value", "intrinsic_value", "time_value", "hedge_ratio"]
        self.result["market"] = [{"name": mkt, "value": self.option[mkt]} for mkt in market_cols]

    def build_price(self):
        price_cols = ["open_price", "max_price", "min_price", "average_price", "close_price", "best_buy_price",
                      "best_sell_price", "transactions", "quantity", "volume"]
        self.result["price"] = [{"name": price, "value": self.option[price]} for price in price_cols]

    def build_option_close_series(self):
        close_price = self.df[["date", "close_price"]].rename(columns={"close_price": "value"})
        self.result["option_close_series"] = close_price.to_dict(orient="records")

    def build_underlying_close_series(self):
        return

    def build_payoff(self):
        self.result["payoff"] = self.payoff