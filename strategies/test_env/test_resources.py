import boto3
from resources import dynamodb_strategies
from resources import strategies_table_name
from data import dynamodb_strategies_data, prepare_item
from aws import dynamodb_client
from aws import aws_credentials
from aws import dynamodb_resource

from boto3.dynamodb.types import TypeDeserializer


deserializer = TypeDeserializer()


def deserialize_item(item):
    return {k: deserializer.deserialize(v) for k, v in item.items()}


def test_dynamo_tables_created(dynamodb_resource, dynamodb_strategies, region_name="us-east-1"):
    """
    Validating if all tables are created on the environment successfully
    Target Table = TB_UNDERLYING_STRATEGIES
    """

    db = boto3.resource("dynamodb", region_name)
    tables = list(db.tables.all())
    assert tables == [dynamodb_resource.Table(strategies_table_name)]


def test_dynamo_strategies_objects_inserted(dynamodb_strategies, region_name="us-east-1"):
    """
    Validating if the mock records were inserted successfully on TB_UNDERLYING_STRATEGIES
    """

    client = boto3.client("dynamodb", region_name)
    data = client.scan(TableName=strategies_table_name).get("Items", [])
    result = [deserialize_item(item) for item in data]
    assert result == dynamodb_strategies_data()
