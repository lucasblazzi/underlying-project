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


def serialize_item(item):
    item = json.loads(json.dumps(item), parse_float=Decimal)
    return {k: serializer.serialize(v) for k, v in item.items()}


def save_item(item, dynamo_client=client):
    item["updatedAt"] = datetime.now().isoformat()
    dynamo_client.put_item(
        TableName=STRATEGIES_TABLE,
        Item=serialize_item(item)
    )
    return item


def validate_item(item):
    return Strategy(**item).dict()


def lambda_handler(event, context):
    try:
        event = json.loads(event["body"])
        strategy = validate_item(event)
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
