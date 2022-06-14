import os
import boto3
import pytest

from data import dynamodb_strategies_data


@pytest.fixture
def s3_option_series(s3_client):
    bucket_name = "underlying-options-series-mock"
    s3_client.create_bucket(Bucket=bucket_name)
    yield


@pytest.fixture
def dynamodb_strategies(dynamodb_resource):
    table_name = "UNDERLYING_STRATEGIES"
    dynamodb_resource.create_table(
        TableName=table_name,
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"}
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    table = dynamodb_resource.Table(table_name)
    [table.put_item(Item=data) for data in dynamodb_strategies_data()]
    table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
    return table
