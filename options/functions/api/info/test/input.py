from copy import deepcopy


base_case = {
    'id': '60137665a3315885b579abe6803b55d0', 
    'name': 'BOVAA100'
    }


class TestSuiteA1:
    """
    A1 - Critério Funcional Sistemático - Classes de Equivalência (C) e Análise do Valor Limite para Opção
        •	Comprimento do nome:
            o	C1 – nome de 5 caracteres  válido
            o	C2 – nome de 8 caracteres  válido
            o	C3 – nome com 2 caracteres  inválido
            o	C4 – nome com 10 caracteres  inválido
            o	C5 – nome vazio  inválido
        •	Tipo do nome:
            o	C6 – nome do tipo string  válido
            o	C7 – nome do tipo inteiro  inválido
            o	C8 – nome do tipo booleano  inválido
        •	Comprimento do id:
            o	C9 – id de 32 caracteres  válido
            o	C10 – id de 31 caracteres  inválido
            o	C11 – id de 33 caracteres  inválido
        •	Tipo do id:
            o	C12 – id do tipo string  válido
            o	C13 – id do tipo dicionário  inválido
            o	C14 – id do tipo booleano  inválido
    """
    @staticmethod
    def input_c1():
        case = deepcopy(base_case)
        case["name"] = "ABCDE"
        return case

    @staticmethod
    def input_c2():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c3():
        case = deepcopy(base_case)
        case["name"] = "AB"
        return case

    @staticmethod
    def input_c4():
        case = deepcopy(base_case)
        case["name"] = "ABCDEFGHIJ"
        return case

    @staticmethod
    def input_c5():
        case = deepcopy(base_case)
        case["name"] = ""
        return case

    @staticmethod
    def input_c6():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c7():
        case = deepcopy(base_case)
        case["name"] = 22
        return case

    @staticmethod
    def input_c8():
        case = deepcopy(base_case)
        case["name"] = True
        return case

    @staticmethod
    def input_c9():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c10():
        case = deepcopy(base_case)
        case["id"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDE"
        return case

    @staticmethod
    def input_c11():
        case = deepcopy(base_case)
        case["id"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFG"
        return case

    @staticmethod
    def input_c12():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c13():
        case = deepcopy(base_case)
        case["id"] = {
            "foo":"bar"
        }
        return case

    @staticmethod
    def input_c14():
        case = deepcopy(base_case)
        case["id"] = False
        return case


class TestSuiteCombinatorial:

    @staticmethod
    def input_ct1():
        # nome válido
        # id válido
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_ct2():
        # nome inválido
        # id válido
        case = deepcopy(base_case)
        case["name"] = "ABC"
        return case

    @staticmethod
    def input_ct3():
        # nome válido
        # id inválido
        case = deepcopy(base_case)
        case["id"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDE"
        return case

    @staticmethod
    def input_ct4():
        # nome inválido
        # id inválido
        case = deepcopy(base_case)
        case["name"] = "ABCDEFGHIJ"
        case["id"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFG"
        return case