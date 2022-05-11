import json


mock = [
    {
        "id": "ITSAD107",
        "name": "ITSAD107",
        "type": "PUT",
        "exercise_price": 9.41,
        "underlying": "ITSA4",
        "expiration_date": "2023-05-03",
        "company": "ITS",
        "close_price": 0.13,
        "greeks": [
            {"name": "gamma", "value": 0.31},
            {"name": "delta", "value": 0.11},
            {"name": "theta", "value": 0.91},
            {"name": "rho", "value": 0.14},
            {"name": "gamma", "value": 0.18},
            {"name": "vega", "value": 0.71},
        ],
        "market": [
            {"name": "option_value", "value": 0.42},
            {"name": "intrinsic_value", "value": 0.19},
            {"name": "time_value", "value": 0.90},
            {"name": "hedge_ration", "value": 0.19},
        ],
        "price": [
            {"name": "open_price", "value": 0.29},
            {"name": "max_price", "value": 0.39},
            {"name": "min_price", "value": 0.28},
            {"name": "average_price", "value": 0.31},
            {"name": "close_price", "value": 0.31},
            {"name": "best_buy_price", "value": 0.28},
            {"name": "best_sell_price", "value": 0.39},
            {"name": "transactions", "value": 1002},
            {"name": "quantity", "value": 401},
            {"name": "volume", "value": 1013},
        ]
    }
]


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(mock)
    }