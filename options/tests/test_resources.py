import boto3
from resources import s3_option_series
from aws import s3_client
from aws import aws_credentials


def test_bucket_options_series_created(s3_option_series, s3_client, region_name="us-east-1"):
    conn = boto3.client("s3", region_name=region_name)
    buckets = [bucket.get("Name") for bucket in conn.list_buckets().get("Buckets")]
    assert buckets == ["underlying-options-series-mock"]