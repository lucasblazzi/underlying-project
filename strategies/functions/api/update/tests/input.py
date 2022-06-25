from copy import deepcopy


base_case = {
    "id": "d5c78622-cc45-4c20-9ada-a34cf39234e1",
    "shared": False
}


class TestSuiteA1:

    @staticmethod
    def input_c1():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c2():
        case = deepcopy(base_case)
        case["shared"] = "Undefined"
        return case
