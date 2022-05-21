import os
import boto3
import json
import asyncio
from html import escape

from .aws.athena import Athena

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


REGION = os.environ.get("REGION", "us-east-1")
ATHENA_DB = os.environ.get("ATHENA_DB", "db_underlying")
OPTIONS_TABLE = os.environ.get("OPTIONS_TABLE", "tb_options_series")
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


async def run_queries(event):
    athena = Athena()
    _input = escape(event["query"])
    query = f"""
        SELECT *
        FROM (
              SELECT id, MAX(date) as max_date
              FROM {ATHENA_DB}.{OPTIONS_TABLE}
              GROUP BY id, date
        ) r
        INNER JOIN {ATHENA_DB}.{OPTIONS_TABLE} t
        ON t.id = r.id AND t.date = r.max_date
        WHERE name LIKE '{_input}%'
        LIMIT 10
    """
    async with athena.session.create_client("athena", region_name=REGION) as athena_client:
        result = await athena.run_query(query, athena_client)
    return result.get(query, {}).get("result", [])


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
    # results = await run_queries(event)
    body = json.loads(event["body"])
    results = query_options(body["query"])
    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))
