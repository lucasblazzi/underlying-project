import json


mock = [
    {
        "id": "BOVAD107",
        "name": "BOVAD107",
        "option_type": "CALL",
        "exercise_price": 123.41,
        "underlying": "BOVA11",
        "expiration_date": "2022-05-03",
        "company": "BOV",
        "close_price": 1.32
    },
    {
        "id": "ITSAD107",
        "name": "ITSAD107",
        "option_type": "PUT",
        "exercise_price": 9.41,
        "underlying": "ITSA4",
        "expiration_date": "2023-05-03",
        "company": "ITS",
        "close_price": 0.13
    }
]


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(mock)
    }