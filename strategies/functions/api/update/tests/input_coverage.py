import json
from copy import deepcopy


base_api_request = {
    "rawPath": "/v1/",
    "body": "{}"
}


class CoverageInput:

    @staticmethod
    def input_update():
        case = deepcopy(base_api_request)
        case["rawPath"] += "update"
        case["body"] = json.dumps({
            "id": "18199ad0-47fb-4592-8fb2-008726efab95",
            "name": "Random Name",
            "strategy": [
                {
                    "name": "custom",
                    "exercise_price": 12.32,
                    "transaction_type": "LONG",
                    "close_price": 1.23,
                    "contracts": 1,
                    "type": "PUT"
                },
                {
                    "name": "custom",
                    "exercise_price": 12.32,
                    "transaction_type": "SHORT",
                    "close_price": 1.23,
                    "contracts": 1,
                    "type": "CAll"
                }
            ]
        })
        return case

    @staticmethod
    def input_delete():
        case = deepcopy(base_api_request)
        case["rawPath"] += "delete"
        case["body"] = json.dumps({
            "id": "18199ad0-47fb-4592-8fb2-008726efab95",
            "deleted": False
        })
        return case

    @staticmethod
    def input_share():
        case = deepcopy(base_api_request)
        case["rawPath"] += "share"
        case["body"] = json.dumps({
            "id": "18199ad0-47fb-4592-8fb2-008726efab95",
            "shared": True
        })
        return case

    @staticmethod
    def input_error_422():
        case = deepcopy(base_api_request)
        case["rawPath"] += "share"
        case["body"] = json.dumps({"id": "1234"})
        return case

    @staticmethod
    def input_error_500():
        case = deepcopy(base_api_request)
        case["rawPath"] += "Invalid"
        return case
