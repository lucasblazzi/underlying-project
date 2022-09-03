import json
from copy import deepcopy


base_api_request = {
    "rawPath": "/v1/",
    "body": "{}"
}


class CoverageInput:

    @staticmethod
    def input_read_strategy():
        case = deepcopy(base_api_request)
        case["rawPath"] += "strategy"
        case["body"] = json.dumps({"id":"18199ad0-47fb-4592-8fb2-008726efab95"})
        return case

    @staticmethod
    def input_read_shared():
        case = deepcopy(base_api_request)
        case["rawPath"] += "shared"
        case["body"] = json.dumps({})
        return case
