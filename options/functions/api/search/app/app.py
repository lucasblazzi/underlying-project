import os
import json
import asyncio
from html import escape

from .aws.athena import Athena
from .aws.es import ES

REGION = os.environ.get("REGION", "us-east-1")
ATHENA_DB = os.environ.get("ATHENA_DB", "db_underlying")
OPTIONS_TABLE = os.environ.get("OPTIONS_TABLE", "tb_options_series")


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


async def query_options(user_input):
    async with ES(index="underlying_options") as client:
        resp = await client.query(query=get_query(user_input))
        print([r["_source"] for r in resp["hits"]["hits"]])
        return [r["_source"] for r in resp["hits"]["hits"]]


async def handler(event):
    # results = await run_queries(event)
    results = await query_options(event["query"])
    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))
