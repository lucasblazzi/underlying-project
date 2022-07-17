from copy import deepcopy
base_case = {
        "event": {
            "body": '{"id": "60137665a3315885b579abe6803b55d0", "name": "BOVAA100"}'
        },
        "context": None
    }


class TestInfo:
   
    @staticmethod
    def input_ok():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_invalid_id():
        case = deepcopy(base_case)
        case['id'] = 'ABCD7665a3315885b579abe6803b55d0'
        return case

    @staticmethod
    def input_invalid_name():
        case = deepcopy(base_case)
        case['name'] = 'ABCDEFGH'
        return case

    @staticmethod
    def input_invalid_dict():
        case = deepcopy(base_case)
        case = {}
        return case
