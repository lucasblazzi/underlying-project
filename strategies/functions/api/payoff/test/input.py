from copy import deepcopy
import json
base_case = {
    'body' : json.dumps({
        "username": "blazzi",
        "name": "Custom Long Straddle",
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
                "transaction_type": "LONG",
                "close_price": 1.23,
                "contracts": 1,
                "type": "CALL"
            },
            {
                "name": "custom",
                "exercise_price": 12.32,
                "transaction_type": "SHORT",
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
                "type": "CALL"
            }
        ]
    })
}


class TestPayoff:
   
    @staticmethod
    def input_valid_strategy():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_invalid_strategy():
        case = deepcopy(base_case)
        case = {}
        return case

    @staticmethod
    def input_no_type_strategy():
        case = deepcopy(base_case)
        temp = json.loads(case['body'])
        del temp['strategy'][0]['type'] 
        case['body'] = json.dumps(temp)
        return case

