from copy import deepcopy
base_case = {
            "statusCode": 200,
            "body": {}
        }


class TestOutput:
   
    @staticmethod
    def ok():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def not_found():
        case = deepcopy(base_case)
        case['statusCode'] = 404
        case['body'] = 'Option not found!'
        return case

    def bad_request():
        case = deepcopy(base_case)
        case['statusCode'] = 400
        case['body'] = 'bad request, body not found at event'
        return case