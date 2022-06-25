import os
import json
from decimal import Decimal
from datetime import datetime

import boto3
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
from pydantic.error_wrappers import ValidationError

from .schema import Option, Share, Delete


serializer = TypeSerializer()
deserializer = TypeDeserializer()

STRATEGIES_TABLE = os.environ.get("STRATEGIES_TABLE", "TB_UNDERLYING_STRATEGIES")


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


class UpdateInterface:
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

    @staticmethod
    def validate_strategy(strategy):
        return [json.loads(json.dumps(Option(**option).dict()), parse_float=Decimal) for option in strategy]

    @staticmethod
    def validate_share(share):
        return Share(**share).dict()

    @staticmethod
    def validate_delete(delete):
        return Delete(**delete).dict()

    def update_item(self, item):
        client = boto3.client('dynamodb')
        item["updatedAt"] = datetime.now().isoformat()
        response = client.update_item(
            TableName=STRATEGIES_TABLE,
            Key=self.prepare_item({"id": item.pop("id")}),
            AttributeUpdates={k: {"Value": serializer.serialize(v), "Action": "PUT"} for k, v in item.items()},
            ReturnValues="ALL_NEW"
        )
        return self.deserialize_item(response["Attributes"])

    def share(self, event):
        update = {
            "id": event["id"],
            "shared": event.get("shared", False)
        }
        res = self.update_item(self.validate_share(update))
        return res

    def delete(self, event):
        update = {
            "id": event["id"],
            "deleted": event.get("deleted", False)
        }
        res = self.update_item(self.validate_delete(update))
        return res

    def update(self, event):
        update = {
            "id": event["id"],
        }
        if event.get("name"):
            update["name"] = event["name"]
        if event.get("strategy"):
            update["strategy"] = self.validate_strategy(event["strategy"])
        res = self.update_item(update)
        return res

    def general_update(self):
        method = self.__get_method()
        event = self.__get_body()
        result = getattr(self, method)(event)
        return result


def lambda_handler(event, context):
    try:
        item = UpdateInterface(event).general_update()
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
            "body": f"Internal Server Error",
            "error": e
        }
