from copy import deepcopy
base_case = {
    "options": [
         {"exercise_price": 12.32, "transaction_type": "SHORT", "close_price": 1.23, "contracts": 1, "type": "CALL"},
         {"exercise_price": 12.32, "transaction_type": "LONG", "close_price": 1.23, "contracts": 1, "type": "CALL"},
         {"exercise_price": 12.32, "transaction_type": "SHORT", "close_price": 1.23, "contracts": 1, "type": "PUT"},
         {"exercise_price": 12.32, "transaction_type": "LONG", "close_price": 1.23, "contracts": 1, "type": "PUT"}],
         "strategy": True}


class TestPayoff:
   
    @staticmethod
    def input_strategy_true():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_strategy_false():
        case = deepcopy(base_case)
        case['strategy'] = False
        return case

    @staticmethod
    def input_invalid_dict():
        case = deepcopy(base_case)
        case = {}
        return case
