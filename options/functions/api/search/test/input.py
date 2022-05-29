

class TestInput:

    @staticmethod
    def lambda_handler_input():
        _input = {
            "event": {
                "body": '{"query": "BOV"}'
            },
            "context": None
        }
        return _input

    @staticmethod
    def handler_input():
        _input = {
            "event": {
                "body": '{"query": "BOV"}'
            }
        }
        return _input

    @staticmethod
    def query_options_input():
        _input = {
            "user_input": "BOV"
        }
        return _input

    @staticmethod
    def get_query_input():
        _input = {
            "query": "BOV"
        }
        return _input
