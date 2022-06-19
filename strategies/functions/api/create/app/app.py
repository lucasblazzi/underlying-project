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

STRATEGIES_TABLE = os.environ.get("STRATEGIES_TABLE", "TB_UNDERLYING_STRATEGIES")


def prepare_item(item):
    item = json.loads(json.dumps(item), parse_float=Decimal)
    return {k: serializer.serialize(v) for k, v in item.items()}


def save_item(item):
    item["updatedAt"] = datetime.now().isoformat()
    client.put_item(
        TableName=STRATEGIES_TABLE,
        Item=prepare_item(item)
    )
    return item


def lambda_handler(event, context):
    try:
        event = json.loads(event["body"])
        strategy = Strategy(**event).dict()
        result = save_item(strategy)
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except ValidationError as e:
        return {
            "statusCode": 422,
            "body": f"Input field validation error: \n{e}"
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": f"Internal Server Error"
        }
