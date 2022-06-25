import json
from decimal import Decimal
from boto3.dynamodb.types import TypeSerializer


serializer = TypeSerializer()


def prepare_item(item):
    item = json.loads(json.dumps(item), parse_float=Decimal)
    return item


def dynamodb_strategies_data():
    obj = [
        {
            "name": "Custom Long Straddle",
            "username": "blazzi",
            "strategy": [
                {
                    "name": "custom",
                    "type": "PUT",
                    "exercise_price": 12.32,
                    "transaction_type": "LONG",
                    "close_price": 1.23,
                    "contracts": 1
                },
                {
                    "name": "custom",
                    "type": "CALL",
                    "exercise_price": 12.32,
                    "transaction_type": "SHORT",
                    "close_price": 1.23,
                    "contracts": 1
                }
            ],
            "id": "18199ad0-47fb-4592-8fb2-008726efab95",
            "shared": False,
            "updatedAt": "2022-06-19T12:54:06.154170"
        }
    ]
    return [prepare_item(item) for item in obj]