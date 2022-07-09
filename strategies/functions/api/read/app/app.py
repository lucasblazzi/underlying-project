import os
import json
from decimal import Decimal

import boto3
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
from pydantic.error_wrappers import ValidationError

from .schema import Strategy


serializer = TypeSerializer()
deserializer = TypeDeserializer()

STRATEGIES_TABLE = os.environ.get("STRATEGIES_TABLE", "TB_UNDERLYING_STRATEGIES")


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


class ReadInterface:
    def __init__(self, event):
        self.event = event

    def __get_body(self):
        return json.loads(self.event["body"])

    def __get_method(self):
        return self.event["rawPath"].split("/")[-1]

    @staticmethod
    def prepare_item(item):
        item = json.loads(json.dumps(item), parse_float=Decimal)
        return {k: serializer.serialize(v) for k, v in item.items()}

    @staticmethod
    def deserialize_item(item):
        return {k: deserializer.deserialize(v) for k, v in item.items()}

    def get_user_strategies(self, event):
        client = boto3.client("dynamodb", region_name="us-east-1")
        response = client.query(
            TableName=STRATEGIES_TABLE,
            IndexName="username-index",
            FilterExpression="deleted=:f and username=:u",
            ExpressionAttributeValues={":f": {"BOOL": False}, ":u": {"S": event["username"]}}
        )
        result = [self.deserialize_item(item) for item in response["Items"]]
        return result

    def get_strategy(self, event):
        client = boto3.client("dynamodb", region_name="us-east-1")
        response = client.get_item(
            TableName=STRATEGIES_TABLE,
            Key={"id": serializer.serialize(event["id"])}
        )
        result = self.deserialize_item(response["Item"])
        return Strategy(**result).dict()

    def get_shared_strategies(self, kwargs):
        client = boto3.client("dynamodb", region_name="us-east-1")
        response = client.scan(
            TableName=STRATEGIES_TABLE,
            FilterExpression="#sh=:t and deleted=:f",
            ExpressionAttributeNames={"#sh": "shared"},
            ExpressionAttributeValues={":t": {"BOOL": True}, ":f": {"BOOL": False}}
        )
        result = [self.deserialize_item(item) for item in response["Items"]]
        return [Strategy(**res).dict() for res in result]

    def general_get(self):
        map_method = {
            "shared": "get_shared_strategies",
            "strategy": "get_strategy",
            "user": "get_user_strategies"
        }
        method = self.__get_method()
        event = self.__get_body()
        result = getattr(self, map_method[method])(event)
        return result


def lambda_handler(event, context):
    try:
        item = ReadInterface(event).general_get()
        return {
            "statusCode": 200,
            "body": json.dumps(item, cls=DecimalEncoder)
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
