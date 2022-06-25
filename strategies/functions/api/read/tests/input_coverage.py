import json
from copy import deepcopy


base_api_request = {
    "rawPath": "/v1/",
    "body": "{}"
}


class CoverageInput:

    @staticmethod
    def input_x():
        case = deepcopy(base_api_request)
        case["rawPath"] += "x"
        case["body"] = json.dumps({})
        return case

    @staticmethod
    def input_y():
        case = deepcopy(base_api_request)
        case["rawPath"] += "y"
        case["body"] = json.dumps({})
        return case
