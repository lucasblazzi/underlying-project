import os
import numpy as np
import json
from json import JSONEncoder

PRICE_RANGE = int(os.environ.get("PRICE_RANGE", 20))


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def get_x(mean_price):
    return np.arange(mean_price - PRICE_RANGE, mean_price + PRICE_RANGE, 1)


def single_payoff(option, x):
    y = []
    scenarios = len(x)
    if option["type"].upper() == 'CALL':
        for i in range(scenarios):
            y.append(max((x[i] - option["exercise_price"] - option["close_price"]), -option["close_price"]))
    else:
        for i in range(scenarios):
            y.append(max(option["exercise_price"] - x[i] - option["close_price"], -option["close_price"]))

    y = np.array(y)
    y = -y if option["transaction_type"] == "SHORT" else y
    return {**option, "x": x, "y": y * option["contracts"]}


def strategy_payoff_calculator(options, x):
    result = list()
    for option in options:
        result.append(single_payoff(option, x))

    strategy = {
        "name": "Strategy",
        "x": x,
        "y": np.mean([n["payoff"] for n in options], axis=0)
    }
    result.append(strategy)
    return result


def lambda_handler(event, context):
    try:
        event = json.loads(event["body"])
        mean_price = np.mean([o["exercise_price"] for o in event["strategy"]])
        x = get_x(mean_price)

        if event.get("calculate_strategy", False):
            result = strategy_payoff_calculator(event["strategy"], x)
        else:
            result = [single_payoff(option, x) for option in event["strategy"]]

        return {
            "statusCode": 200,
            "body": json.dumps(result, cls=NumpyArrayEncoder)
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": f"Internal Server Error"
        }
