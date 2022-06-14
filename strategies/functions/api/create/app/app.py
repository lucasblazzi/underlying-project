import os
import json
from decimal import Decimal
from datetime import datetime

import boto3
from boto3.dynamodb.types import TypeSerializer
from pydantic.error_wrappers import ValidationError

from .schema import Strategy


client = boto3.client('dynamodb')
serializer = TypeSerializer()

STRATEGIES_TABLE = os.environ.get("STRATEGIES_TABLE", "UNDERLYING_STRATEGIES")


def prepare_item(item):
    item = json.loads(json.dumps(item), parse_float=Decimal)
    return {k: serializer.serialize(v) for k, v in item.items()}


def save_item(item):
    item["updatedAt"] = datetime.now().isoformat()
    response = client.put_item(
        TableName=STRATEGIES_TABLE,
        Item=prepare_item(item)
    )
    return response


def lambda_handler(event, context):
    try:
        event = json.loads(event)
        strategy = Strategy(**event).dict()
        save_item(strategy)
    except ValidationError as e:
        return {
            "statusCode": 422,
            "body": f"Missing required fields: \n{e}"
        }


# event = json.dumps({
#     "username": "blazzi",
#     "strategy": [
#         {
#             "id": "custom",
#             "name": "custom",
#             "exercise_price": 12.32,
#             "transaction_type": "LONG",
#             "close_price": 1.23,
#             "contracts": 1,
#             "type": "CAll"
#         },
#         {
#             "id": "custom",
#             "name": "custom",
#             "exercise_price": 12.32,
#             "transaction_type": "SHORT",
#             "close_price": 1.23,
#             "contracts": 1,
#             "type": "CAll"
#         }
#     ]
# })
# print(lambda_handler(event, ""))