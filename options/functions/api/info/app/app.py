import os
import json
import asyncio

import pandas as pd
from aiobotocore.session import get_session

session = get_session()


SERIES_BUCKET = os.environ.get("SERIES_BUCKET", "underlying-options-series")
REGION = os.environ.get("REGION", "us-east-1")
PAYOFF_LAMBDA = os.environ.get("PAYOFF_LAMBDA", "OPTIONS-SERVICES-PAYOFF")


mock = [
    {
        "id": "ITSAD107",
        "name": "ITSAD107",
        "type": "PUT",
        "exercise_price": 9.41,
        "underlying": "ITSA4",
        "expiration_date": "2023-05-03",
        "company": "ITAÚ",
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
        ],
        "option_close_series": [
            {"date": "2022-01-01", "value": 2.34},
            {"date": "2022-02-01", "value": 2.38},
            {"date": "2022-03-01", "value": 2.32},
            {"date": "2022-04-01", "value": 2.27},
            {"date": "2022-05-01", "value": 2.30},
            {"date": "2022-06-01", "value": 2.28},
            {"date": "2022-07-01", "value": 2.36},
        ],
        "underlying_close_series": [
            {"date": "2022-01-01", "value": 21.34},
            {"date": "2022-02-01", "value": 22.38},
            {"date": "2022-03-01", "value": 23.32},
            {"date": "2022-04-01", "value": 26.27},
            {"date": "2022-05-01", "value": 21.30},
            {"date": "2022-06-01", "value": 23.28},
            {"date": "2022-07-01", "value": 25.36},
        ],
        "payoff": {
          "strategy": {
            "payoff": [
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "x": [
              -7.68,
              -6.68,
              -5.68,
              -4.68,
              -3.6799999999999997,
              -2.6799999999999997,
              -1.6799999999999997,
              -0.6799999999999997,
              0.3200000000000003,
              1.3200000000000003,
              2.3200000000000003,
              3.3200000000000003,
              4.32,
              5.32,
              6.32,
              7.32,
              8.32,
              9.32,
              10.32,
              11.32,
              12.32,
              13.32,
              14.32,
              15.32,
              16.32,
              17.32,
              18.32,
              19.32,
              20.32,
              21.32,
              22.32,
              23.32,
              24.32,
              25.32,
              26.32,
              27.32,
              28.32,
              29.32,
              30.32,
              31.32
            ]
          },
          "options": [
            {
              "exercise_price": 12.32,
              "transaction_type": "LONG",
              "close_price": 1.23,
              "contracts": 1,
              "type": "CAll",
              "payoff": [
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -1.23,
                -0.22999999999999998,
                0.77,
                1.77,
                2.77,
                3.77,
                4.77,
                5.77,
                6.77,
                7.77,
                8.77,
                9.77,
                10.77,
                11.77,
                12.77,
                13.77,
                14.77,
                15.77,
                16.77,
                17.77
              ]
            },
            {
              "exercise_price": 12.32,
              "transaction_type": "SHORT",
              "close_price": 1.23,
              "contracts": 1,
              "type": "CAll",
              "payoff": [
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                1.23,
                0.22999999999999998,
                -0.77,
                -1.77,
                -2.77,
                -3.77,
                -4.77,
                -5.77,
                -6.77,
                -7.77,
                -8.77,
                -9.77,
                -10.77,
                -11.77,
                -12.77,
                -13.77,
                -14.77,
                -15.77,
                -16.77,
                -17.77
              ]
            }
          ]
        }
    }
]


def preprocess_payload(option):
    payload = {"options": [], "strategy": False}
    transaction_types = ("SHORT", "LONG")
    for t in transaction_types:
        tmp_opt = {
            "exercise_price": option["exercise_price"],
            "close_price": option["close_price"],
            "contracts": 1,
            "type": option["type"],
            "transaction_type": t
        }
        payload["options"].append(tmp_opt)
    return payload


async def get_option(option):
    return pd.read_parquet(f"s3://{SERIES_BUCKET}/name={option['name']}/{option['id']}.snappy.parquet")


async def get_payoff(option):
    async with session.create_client("lambda", region_name=REGION) as client:
        response = await client.invoke(
            FunctionName=PAYOFF_LAMBDA,
            InvocationType="RequestResponse",
            Payload=json.dumps(preprocess_payload(option))
        )
        result = await response["Payload"].read()
    return json.loads(result.decode("utf-8"))


async def handler(event):
    # option = pd.DataFrame(await get_option(event)).sort_values("date")
    # payoff_option = option.iloc[-1].to_dict()
    # payoff = await get_payoff(payoff_option)
    # x = 0
    return {
        "statusCode": 200,
        "body": json.dumps(mock)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))


event = {
    "name": "BOVAA100",
    "id": "5153291b1c140f84eddd6b4c9410b82b"
}
print(lambda_handler(event, ""))
