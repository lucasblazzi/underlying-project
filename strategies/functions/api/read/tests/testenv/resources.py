import pytest
from .data import dynamodb_strategies_data
from .aws import aws_credentials, dynamodb_resource


strategies_table_name = "TB_UNDERLYING_STRATEGIES"


@pytest.fixture
def dynamodb_strategies(aws_credentials, dynamodb_resource, region_name="us-east-1"):
    dynamodb_resource.create_table(
        TableName=strategies_table_name,
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"}
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    table = dynamodb_resource.Table(strategies_table_name)
    [table.put_item(Item=data) for data in dynamodb_strategies_data()]
    table.meta.client.get_waiter("table_exists").wait(TableName=strategies_table_name)
    return table
