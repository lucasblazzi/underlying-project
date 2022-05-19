import os
import json
import asyncio

import pandas as pd
from aiobotocore.session import get_session

from .builder import OptionBuilder

session = get_session()


SERIES_BUCKET = os.environ.get("SERIES_BUCKET", "underlying-options-series")
REGION = os.environ.get("REGION", "us-east-1")
PAYOFF_LAMBDA = os.environ.get("PAYOFF_LAMBDA", "OPTIONS-SERVICES-PAYOFF")


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
    body = json.loads(event["body"])
    option_series = pd.DataFrame(await get_option(body)).sort_values("date")
    option = option_series.iloc[-1]
    payoff = await get_payoff(option.to_dict())
    result = OptionBuilder(option_series, option, payoff).build
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))
