import os
import boto3
import json
import asyncio
from html import escape

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


REGION = os.environ.get("REGION", "us-east-1")
ES_HOST = os.environ.get("ES_HOST", "https://search-underlying-zpfrcbjukmsi3otoeaohoemdu4.us-east-1.es.amazonaws.com")


credentials = boto3.Session().get_credentials()
auth = AWS4Auth(credentials.access_key, credentials.secret_key,
                REGION, "es", session_token=credentials.token)

es = Elasticsearch(
    f"{ES_HOST}:443",
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)


def get_query(query):
    return {
        "from": 0,
        "size": 20,
        "query": {
            "match_phrase_prefix": {
                "name": escape(query)
            }
        }
    }


def query_options(user_input):
    resp = es.search(body=get_query(user_input), index="underlying_options")
    return [r["_source"] for r in resp["hits"]["hits"]]


async def handler(event):
    body = json.loads(event["body"])
    results = query_options(body["query"])
    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))
