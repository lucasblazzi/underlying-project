import os
import boto3
import json
import asyncio
from html import escape

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


REGION = os.environ.get("REGION", "us-east-1")
ES_HOST = os.environ.get("ES_HOST", "https://search-underlying-zpfrcbjukmsi3otoeaohoemdu4.us-east-1.es.amazonaws.com")

# mock = [{"date": "2022-01-14", "id": "fe3d332653653d61b841ba24e10f82a8", "name": "ITSAA110", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 10.35, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "3f019e6b4ceab29dd1a05f71198e33b1", "name": "ITSAA114", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 10.59, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "8f842cf0bb96ab81ae349eeb74f07df3", "name": "ITSAA123", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 11.54, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-19", "id": "2caade6e4449a77eecb27f30c5fa2bb4", "name": "ITSAA148", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 13.81, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "2857ea0b4b883425440709ddc57df3e4", "name": "ITSAA869", "name_underlying": "ITSA4", "close_price": 1.6, "exercise_price": 8.11, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "9a9073e75e6253b4b65a29cb78b7e325", "name": "ITSAA889", "name_underlying": "ITSA4", "close_price": 1.34, "exercise_price": 8.3, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-13", "id": "054a9a51a8284c274994b923bd340d9c", "name": "ITSAA909", "name_underlying": "ITSA4", "close_price": 0.95, "exercise_price": 8.5, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-21", "id": "8c4fffff01d2ce28902448f2d66c770d", "name": "ITSAA929", "name_underlying": "ITSA4", "close_price": 1.03, "exercise_price": 8.58, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-05-23", "id": "095d7b16a8f2fdf08fd9105cbed715b2", "name": "ITSAA930", "name_underlying": "ITSA4", "close_price": 2.46, "exercise_price": 9.3, "expiration_date": "2024-01-19", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-21", "id": "2db47f1bb773817d062edda3e4941c8d", "name": "ITSAA949", "name_underlying": "ITSA4", "close_price": 0.8, "exercise_price": 8.77, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "4f4a6f17a007858438cae66767d3431e", "name": "ITSAA969", "name_underlying": "ITSA4", "close_price": 0.71, "exercise_price": 9.07, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "13da9e6e1a231e4eac889e0e014acf06", "name": "ITSAA980", "name_underlying": "ITSA4", "close_price": 0.4, "exercise_price": 9.26, "expiration_date": "2022-01-21", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-05-19", "id": "a5977f379d10b9d515f0615de85f4b16", "name": "ITSAB110", "name_underlying": "ITSA4", "close_price": 0.9, "exercise_price": 10.1, "expiration_date": "2023-02-17", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-17", "id": "0de2771e2a6f9ef941297d926f48ec7c", "name": "ITSAB119", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 11.14, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-03", "id": "565af887f0cd41f765644bb6a4de4979", "name": "ITSAB120", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 11.72, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-17", "id": "112f940c9f584e09c3a8b26aaba1fe1b", "name": "ITSAB130", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 12.57, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-07", "id": "4a926d1b8cdbeba26ee02828b392e02a", "name": "ITSAB135", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 13.15, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-08", "id": "b39e4ffcbd176087e805cd968a09c369", "name": "ITSAB140", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 13.52, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-17", "id": "cb030749d99b5c6be2280bfb670df85d", "name": "ITSAB885", "name_underlying": "ITSA4", "close_price": 2.24, "exercise_price": 8.28, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "c3a6137e36b7ded984a017c5b5e17a80", "name": "ITSAB920", "name_underlying": "ITSA4", "close_price": 1.23, "exercise_price": 8.58, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-01-14", "id": "7973e392e27ef548ee3e09d5ac794745", "name": "ITSAB925", "name_underlying": "ITSA4", "close_price": 1.05, "exercise_price": 8.77, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-18", "id": "f19113da6520f0517dd3aa3aea832373", "name": "ITSAB945", "name_underlying": "ITSA4", "close_price": 1.67, "exercise_price": 8.85, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-18", "id": "65bc4e1affcb9b5fe6354d0d0a72f04d", "name": "ITSAB965", "name_underlying": "ITSA4", "close_price": 1.51, "exercise_price": 9.04, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-18", "id": "e7b6119fa637ad3b861934d27820ba9e", "name": "ITSAB985", "name_underlying": "ITSA4", "close_price": 1.27, "exercise_price": 9.23, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-02-18", "id": "172a85b463c01530140ad3cbaa058fa2", "name": "ITSAB991", "name_underlying": "ITSA4", "close_price": 0.63, "exercise_price": 9.91, "expiration_date": "2022-02-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-03-18", "id": "ecd639f456feb2b1439840eef4796c33", "name": "ITSAC103", "name_underlying": "ITSA4", "close_price": 0.12, "exercise_price": 10.19, "expiration_date": "2022-03-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-03-18", "id": "b38f41f49142fc246929c266b96dad18", "name": "ITSAC11", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 11.56, "expiration_date": "2022-03-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-03-18", "id": "0899462ff67d7ae817f5da015628871e", "name": "ITSAC115", "name_underlying": "ITSA4", "close_price": 0.01, "exercise_price": 10.68, "expiration_date": "2022-03-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-03-11", "id": "dc63a8afe41d06ab692fe509baf0762e", "name": "ITSAC219", "name_underlying": "ITSA4", "close_price": 0.54, "exercise_price": 9.36, "expiration_date": "2022-03-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}, {"date": "2022-03-14", "id": "0e3dd0b1ce46bdb6eb9f44fa9a7f0ad6", "name": "ITSAC224", "name_underlying": "ITSA4", "close_price": 0.42, "exercise_price": 9.56, "expiration_date": "2022-03-18", "type": "CALL", "isin_code": "BRITSAACNPR7"}]
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


def get_query(user_input):
    return {
        "from": user_input.get("from", 0),
        "size": user_input.get("size", 10),
        "query": {
            "match_phrase_prefix": {
                "name": escape(user_input["query"])
            }
        }
    }


def query_options(user_input):
    resp = es.search(body=get_query(user_input), index="underlying_options")
    return [r["_source"] for r in resp["hits"]["hits"]]


async def handler(event):
    body = json.loads(event["body"])
    results = query_options(body)
    # results = mock
    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))
