from copy import deepcopy

base_case = {
    "id": "d5c78622-cc45-4c20-9ada-a34cf39234e1",
    "shared": False
}

base_case2 = {
    "id": "d5c78622-cc45-4c20-9ada-a34cf39234e1",
    "deleted": False
}

base_caseC1 = {
    "id": "cc45-d5c78622-a34cf39234e1-4c20-9ada",
    "shared": True
}

base_caseC2 = {
    "id": "4c20-d5c78622-9ada-a34cf39234e1-cc45",
    "deleted": True
}


class TestSuiteA1:

    @staticmethod
    def input_c1():
        case = deepcopy(base_case)
        return case
    
    @staticmethod
    def input_c2():
        case = deepcopy(base_case)
        case["id"]= "d5c78622-cc45-4c20-9ada-a34cf39234e"
        return case

    @staticmethod
    def input_c3():
        case = deepcopy(base_case)
        case["id"]= "d5c78622-cc45-4c20-9ada-a34cf39234e12"
        return case

    @staticmethod
    def input_c4():
        case = deepcopy(base_case)
        case["id"]= "d"
        return case

    @staticmethod
    def input_c5():
        case = deepcopy(base_case)
        case["id"]= "Undefined"
        return case

    @staticmethod
    def input_c6():
        case = deepcopy(base_case)
        case["id"] = "5dc78622-cc45-4c20-9ada-a34cf392341e"
        return case

    @staticmethod
    def input_c7():
        case = deepcopy(base_case)
        case["id"] =  10
        return case

    @staticmethod
    def input_c8():
        case = deepcopy(base_case)
        case["id"] =  False
        return case

    @staticmethod
    def input_c9():
        case = deepcopy(base_case)
        case["id"] =  2.134
        return case


    @staticmethod
    def input_c10():
        case = deepcopy(base_case)
        case["shared"] = True
        return case

    @staticmethod
    def input_c11():
        case = deepcopy(base_case)
        case["shared"] = 50
        return case

    @staticmethod
    def input_c12():
        case = deepcopy(base_case)
        case["shared"] = "teste"
        return case

    @staticmethod
    def input_c13():
        case = deepcopy(base_case)
        case["shared"] = ""
        return case

class TestSuiteA2:

    @staticmethod
    def input_c14():
        case = deepcopy(base_case2)
        return case
    
    @staticmethod
    def input_c15():
        case = deepcopy(base_case2)
        case["id"]= "d5c78622-cc45-4c20-9ada-a34cf39234e"
        return case

    @staticmethod
    def input_c16():
        case = deepcopy(base_case2)
        case["id"]= "d5c78622-cc45-4c20-9ada-a34cf39234e12"
        return case

    @staticmethod
    def input_c17():
        case = deepcopy(base_case2)
        case["id"]= "d"
        return case

    @staticmethod
    def input_c18():
        case = deepcopy(base_case2)
        case["id"]= "Undefined"
        return case

    @staticmethod
    def input_c19():
        case = deepcopy(base_case2)
        case["id"] = "5dc78622-cc45-4c20-9ada-a34cf392341e"
        return case

    @staticmethod
    def input_c20():
        case = deepcopy(base_case2)
        case["id"] =  10
        return case

    @staticmethod
    def input_c21():
        case = deepcopy(base_case2)
        case["id"] =  False
        return case

    @staticmethod
    def input_c22():
        case = deepcopy(base_case2)
        case["id"] =  2.134
        return case


    @staticmethod
    def input_c23():
        case = deepcopy(base_case2)
        case["deleted"] = True
        return case

    @staticmethod
    def input_c24():
        case = deepcopy(base_case2)
        case["deleted"] = 50
        return case

    @staticmethod
    def input_c25():
        case = deepcopy(base_case2)
        case["deleted"] = "teste"
        return case

    @staticmethod
    def input_c26():
        case = deepcopy(base_case2)
        case["deleted"] = ""
        return case

class TestSuiteCombinatorial:

    @staticmethod
    def input_tc01():
        case = deepcopy(base_caseC1)#share
        return case

    @staticmethod
    def input_tc02():
        case = deepcopy(base_caseC2)#delete
        return case

    @staticmethod
    def input_tc03():
        case = deepcopy(base_caseC1)
        case["shared"] = "Azul"
        return case

    @staticmethod
    def input_tc04():
        case = deepcopy(base_caseC1)
        case["id"] =  43001
        return case
    
    @staticmethod
    def input_tc05():
        case = deepcopy(base_caseC1)
        case["id"] = "sim"
        case["shared"] = "sim"
        return case
    
    @staticmethod
    def input_tc06():
        case = deepcopy(base_caseC2)
        case["deleted"] = "ok"
        return case

    @staticmethod
    def input_tc07():
        case = deepcopy(base_caseC2)
        case["id"] = "5$8ierFF"
        return case
    
    @staticmethod
    def input_tc08():
        case = deepcopy(base_caseC2)
        case["id"] = "no"
        case["shared"] = "no"
        return case
