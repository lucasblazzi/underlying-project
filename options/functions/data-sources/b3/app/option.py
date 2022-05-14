import numpy as np
from scipy.stats import norm


RISK_FREE_RATE = 0.04


class Option:

    """
    Structure:
        type (call / put)
        exercise_price
        close_price_underlying
        volatility_underlying  (decimal)
        risk_free_rate  (decimal)
        expiration_time (years)

    Outputs:
        Implied Volatility: Represents the market's view of the likelihood that an asset's price will change

        Intrinsic Value: Compare the price of the underlying stock or asset to the option strike price (only > 0 - in the money)

        Delta: Measure of the change in an option's price (that is, the premium of an option) resulting from a change in the underlying security
               Also used when determining directional risk. Positive deltas are long (buy) market assumptions, negative deltas are short (sell) market assumptions, and neutral deltas are neutral market assumptions
               Delta tends to increase closer to expiration for near or at-the-money options.
               Delta is further evaluated by gamma, which is a measure of delta's rate of change.
               Delta can also change in reaction to implied volatility changes.
               Can represents the probability the option will finish in the money (delta = 0.25, 25% chance of finishing in the money)

        Hedge Ratio: number of option contracts to underlying contracts for hedging (1/delta)

        Gamma: Rate of change in delta as the underlying price changes
               Calls and puts with the same exercise price and time to expiration have the same gamma

    """

    def __init__(self, df):
        self.df = df

    def n1(self):
        self.df["n1"] = np.log(self.df["close_price_underlying"] / self.df["exercise_price"])

    def n2(self):
        self.df["n2"] = (RISK_FREE_RATE + (np.power(self.df["volatility_underlying"], 2)/2)) * self.df["expiration_time"]

    def d(self):
        self.df["d"] = self.df["volatility_underlying"] * (np.sqrt(self.df["expiration_time"]))

    def d1(self):
        self.df["d1"] = (self.df["n1"] + self.df["n2"]) / self.df["d"]

    def d2(self):
        self.df["d2"] = self.df["d1"] - (self.df["volatility_underlying"] * np.sqrt(self.df["expiration_time"]))

    def gamma(self):
        self.df["gamma"] = (np.exp(-np.power(self.df["d1"], 2) / 2)) / \
                           (self.df["close_price_underlying"] * self.df["volatility_underlying"] *
                            np.sqrt(2 * np.pi * self.df["expiration_time"]))

    def vega(self):
        self.df["vega"] = (self.df["close_price_underlying"] * np.sqrt(self.df["expiration_time"]) *
                           np.exp(-np.power(self.df["d1"], 2) / 2)) / (np.sqrt(2 * np.pi) * 100)

    def a(self):
        self.df["a"] = self.df["close_price_underlying"] * self.df["normal_d1"]

    def b(self):
        self.df["b"] = (self.df["exercise_price"] * self.df["normal_d2"] *
                        (np.exp(-RISK_FREE_RATE * self.df["expiration_time"])))

    def time_value(self):
        self.df["time_value"] = self.df["option_value"] - self.df["intrinsic_value"]

    def hedge_ratio(self):
        self.df["hedge_ratio"] = 1 / self.df["delta"]

    @property
    def features(self):
        self.n1()
        self.n2()
        self.d()
        self.d1()
        self.d2()
        self.normal_d1()
        self.normal_d2()
        self.a()
        self.b()
        self.option_value()
        self.intrinsic_value()
        self.time_value()
        self.delta()
        self.theta()
        self.rho()
        self.gamma()
        self.vega()
        self.hedge_ratio()
        return self.df


class OptionCall(Option):

    """
    Input: dataframe of call options following class Option structure
    """

    def __init__(self, df):
        super().__init__(df)

    def normal_d1(self):
        self.df["normal_d1"] = norm.cdf(self.df["d1"])

    def normal_d2(self):
        self.df["normal_d2"] = norm.cdf(self.df["d2"])

    def option_value(self):
        self.df["option_value"] = self.df["a"] - self.df["b"]

    def intrinsic_value(self):
        self.df["intrinsic_value"] = np.maximum(0, self.df["close_price_underlying"] - self.df["exercise_price"])

    def delta(self):
        self.df["delta"] = self.df["normal_d1"]

    def theta(self):
        self.df["theta"] = (-((self.df["close_price_underlying"] * self.df["volatility_underlying"] * np.exp(-np.power(self.df["d1"], 2) / 2)) /
                              (np.sqrt(8 * np.pi * self.df["expiration_time"]))) -
                            (self.df["normal_d2"] * RISK_FREE_RATE * self.df["exercise_price"]
                             * np.exp(-RISK_FREE_RATE * self.df["expiration_time"])))/365

    def rho(self):
        self.df["rho"] = self.df["expiration_time"] * self.df["exercise_price"] * self.df["normal_d2"] * \
                         np.exp(-RISK_FREE_RATE * self.df["expiration_time"])/100


class OptionPut(Option):

    """
    Input: dataframe of put options following class Option structure
    """

    def __init__(self, df):
        super().__init__(df)

    def normal_d1(self):
        self.df["normal_d1"] = norm.cdf(-self.df["d1"])

    def normal_d2(self):
        self.df["normal_d2"] = norm.cdf(-self.df["d2"])

    def option_value(self):
        self.df["option_value"] = self.df["b"] - self.df["a"]

    def intrinsic_value(self):
        self.df["intrinsic_value"] = np.maximum(0, self.df["exercise_price"] - self.df["close_price_underlying"])

    def delta(self):
        self.df["delta"] = -self.df["normal_d1"]

    def theta(self):
        self.df["theta"] = (-((self.df["close_price_underlying"] * self.df["volatility_underlying"] * np.exp(-np.power(self.df["d1"], 2) / 2)) /
                              (np.sqrt(8 * np.pi * self.df["expiration_time"]))) +
                            (self.df["normal_d2"] * RISK_FREE_RATE * self.df["exercise_price"]
                             * np.exp(-RISK_FREE_RATE * self.df["expiration_time"])))/365

    def rho(self):
        self.df["rho"] = -self.df["expiration_time"] * self.df["exercise_price"] * self.df["normal_d2"] * \
                         np.exp(-RISK_FREE_RATE * self.df["expiration_time"])/100