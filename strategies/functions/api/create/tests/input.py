from copy import deepcopy


base_case = {
    "username": "blazzi",
    "name": "Estratégia de validação Long Straddle",
    "strategy": [
        {
            "name": "CUSTS12",
            "exercise_price": 12.32,
            "transaction_type": "LONG",
            "close_price": 11.24,
            "contracts": 1,
            "type": "PUT"
        }
    ]
}


class TestSuiteA1:
    """
    A1 - Critério Funcional Sistemático - Classes de Equivalência (C) e Análise do Valor Limite para estratégia
        •	Comprimento do nome:
            o	C1 – nome de 3 caracteres  válido
            o	C2 – nome de 40 caracteres  válido
            o	C3 – nome com 2 caracteres  inválido
            o	C4 – nome com 41 caracteres  inválido
            o	C5 – nome vazio  inválido
        •	Tipo do nome:
            o	C6 – nome do tipo string  válido
            o	C7 – nome do tipo inteiro  inválido
            o	C8 – nome do tipo booleano  inválido
        •	Comprimento de opções:
            o	C9 – opções com 1 item  válido
            o	C10 – opções com 2 itens  válido
            o	C11 – opções vazio  inválido
        •	Tipo de opções:
            o	C12 – opções do tipo lista  válido
            o	C13 – opções do tipo dicionário  inválido
            o	C14 – opções do tipo null  inválido
        •	Comprimento do username:
            o	C15 – username de 6 caracteres  válido
            o	C16 – username de 20 caracteres  válido
            o	C17 – username com 5 caracteres  inválido
            o	C18 – username com 21 caracteres  inválido
            o	C19 – username vazio  inválido
        •	Tipo do username:
            o	C20 – username do tipo string  válido
            o	C21 – username do tipo inteiro  inválido
            o	C22 – username do tipo booleano  inválido
    """
    @staticmethod
    def input_c1():
        case = deepcopy(base_case)
        case["name"] = "ABC"
        return case

    @staticmethod
    def input_c2():
        case = deepcopy(base_case)
        case["name"] = "Estratégia de validação Long Straddle 22"
        return case

    @staticmethod
    def input_c3():
        case = deepcopy(base_case)
        case["name"] = "22"
        return case

    @staticmethod
    def input_c4():
        case = deepcopy(base_case)
        case["name"] = "Estratégia de validação Long Straddle 022"
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
        case["strategy"].append(
            {
                "name": "CUSTB12 - SHORT",
                "exercise_price": 12.32,
                "transaction_type": "SHORT",
                "close_price": 1.23,
                "contracts": 1,
                "type": "CALL"
            }
        )
        return case

    @staticmethod
    def input_c11():
        case = deepcopy(base_case)
        case["strategy"] = []
        return case

    @staticmethod
    def input_c12():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c13():
        case = deepcopy(base_case)
        case["strategy"] = {
            "name": "CUSTS12 - LONG",
            "exercise_price": 12.32,
            "transaction_type": "LONG",
            "close_price": 1.23,
            "contracts": 1,
            "type": "PUT"
        }
        return case

    @staticmethod
    def input_c14():
        case = deepcopy(base_case)
        case["strategy"] = None
        return case

    @staticmethod
    def input_c15():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c16():
        case = deepcopy(base_case)
        case["username"] = "lucas_tiense_blazzi1"
        return case

    @staticmethod
    def input_c17():
        case = deepcopy(base_case)
        case["username"] = "joao1"
        return case

    @staticmethod
    def input_c18():
        case = deepcopy(base_case)
        case["username"] = "lucas_tiense_blazzi22"
        return case

    @staticmethod
    def input_c19():
        case = deepcopy(base_case)
        case["username"] = ""
        return case

    @staticmethod
    def input_c20():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c21():
        case = deepcopy(base_case)
        case["username"] = 22
        return case

    @staticmethod
    def input_c22():
        case = deepcopy(base_case)
        case["username"] = True
        return case


class TestSuiteA2:
    """
    A2 - Critério Funcional Sistemático - Classes de Equivalência (C) e Análise do Valor Limite para opção
        •	Comprimento do nome:
            o	C23 – nome de 3 caracteres  válido
            o	C24 – nome de 40 caracteres  válido
            o	C25 – nome com 2 caracteres  inválido
            o	C26 – nome com 41 caracteres  inválido
            o	C27 – nome vazio  inválido
        •	Tipo do nome:
            o	C28 – nome do tipo string  válido
            o	C29 – nome do tipo inteiro  inválido
            o	C30 – nome do tipo booleano  inválido
        •	Tipo do tipo:
            o	C31 – tipo do tipo string  válido
            o	C32 – tipo do tipo inteiro  inválido
            o	C33 – tipo do tipo null  inválido
        •	Valores do tipo:
            o	C34 – valor do tipo é CALL  válido
            o	C35 – nome do tipo é PUT  válido
            o	C36 – valor do tipo é call  válido
            o	C37 – valor do tipo é long  inválido
        •	Tipo do preço de exercício:
            o	C38 – tipo do preço de exercicío float  válido
            o	C39 – tipo do preço de exercicío string  inválido
            o	C40 – tipo do preço de exercicío null  inválido
        •	Valores do preço de exercício:
            o	C41 – valor do preço de exercício é 12,34  válido
            o	C42 – valor do preço de exercício é -12,34  inválido
            o	C42 – valor do preço de exercício é 0  inválido
        •	Tipo do tipo da transação:
            o	C43 – tipo do tipo da transação string  válido
            o	C44 – tipo do tipo da transação float  inválido
            o	C45 – tipo do tipo da transação null  inválido
        •	Valores do tipo da transação:
            o	C46 – valor do tipo da transação é LONG  válido
            o	C47 – nome do tipo da transação é SHORT  válido
            o	C48 – valor do tipo da transação é short  válido
            o	C49 – valor do tipo da transação é CALL  inválido
        •	Tipo do preço de fechamento:
            o	C50 – tipo do preço de fechamento float  válido
            o	C51 – tipo do preço de fechamento string  inválido
            o	C52 – tipo do preço de fechamento null  inválido
        •	Valores do preço de fechamento:
            o	C53 – valor do preço de fechamento é 11,24  válido
            o	C54 – valor do preço de fechamento é -11,24  inválido
            o	C55 – valor do preço de fechamento é 0  inválido
        •	Tipo do contratos:
            o	C56 – tipo do contratos inteiro  válido
            o	C57 – tipo do contratos string  inválido
            o	C58 – tipo do contratos null  inválido
        •	Valores do contratos:
            o	C59 – valor do contratos é 100  válido
            o	C60 – valor do contratos é -34  inválido
            o	C61 – valor do contratos é 80.42  inválido
            o	C62 – valor do contratos é 0  inválido
    """

    @staticmethod
    def input_c23():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = "ITS"
        return case

    @staticmethod
    def input_c24():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = "RDNS13 - Random Undelying - Exercise: 12"
        return case

    @staticmethod
    def input_c25():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = "RD"
        return case

    @staticmethod
    def input_c26():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = "RDNS13 - Random Undelying - Exercise: 12,89"
        return case

    @staticmethod
    def input_c27():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = ""
        return case

    @staticmethod
    def input_c28():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c29():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = 13
        return case

    @staticmethod
    def input_c30():
        case = deepcopy(base_case)
        case["strategy"][0]["name"] = True
        return case

    @staticmethod
    def input_c31():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c32():
        case = deepcopy(base_case)
        case["strategy"][0]["type"] = 1
        return case

    @staticmethod
    def input_c33():
        case = deepcopy(base_case)
        case["strategy"][0]["type"] = None
        return case

    @staticmethod
    def input_c34():
        case = deepcopy(base_case)
        case["strategy"][0]["type"] = "CALL"
        return case

    @staticmethod
    def input_c35():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c36():
        case = deepcopy(base_case)
        case["strategy"][0]["type"] = "call"
        return case

    @staticmethod
    def input_c37():
        case = deepcopy(base_case)
        case["strategy"][0]["type"] = "long"
        return case

    @staticmethod
    def input_c38():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c39():
        case = deepcopy(base_case)
        case["strategy"][0]["exercise_price"] = "invalid"
        return case

    @staticmethod
    def input_c40():
        case = deepcopy(base_case)
        case["strategy"][0]["exercise_price"] = None
        return case

    @staticmethod
    def input_c41():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c42():
        case = deepcopy(base_case)
        case["strategy"][0]["exercise_price"] = -12.34
        return case

    @staticmethod
    def input_c43():
        case = deepcopy(base_case)
        case["strategy"][0]["exercise_price"] = 0
        return case

    @staticmethod
    def input_c44():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c45():
        case = deepcopy(base_case)
        case["strategy"][0]["transaction_type"] = 123.41
        return case

    @staticmethod
    def input_c46():
        case = deepcopy(base_case)
        case["strategy"][0]["transaction_type"] = None
        return case

    @staticmethod
    def input_c47():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c48():
        case = deepcopy(base_case)
        case["strategy"][0]["transaction_type"] = "SHORT"
        return case

    @staticmethod
    def input_c49():
        case = deepcopy(base_case)
        case["strategy"][0]["transaction_type"] = "short"
        return case

    @staticmethod
    def input_c50():
        case = deepcopy(base_case)
        case["strategy"][0]["transaction_type"] = "CALL"
        return case

    @staticmethod
    def input_c51():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c52():
        case = deepcopy(base_case)
        case["strategy"][0]["close_price"] = "invalid"
        return case

    @staticmethod
    def input_c53():
        case = deepcopy(base_case)
        case["strategy"][0]["close_price"] = None
        return case

    @staticmethod
    def input_c54():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c55():
        case = deepcopy(base_case)
        case["strategy"][0]["close_price"] = -11.24
        return case

    @staticmethod
    def input_c56():
        case = deepcopy(base_case)
        case["strategy"][0]["close_price"] = 0
        return case

    @staticmethod
    def input_c57():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c58():
        case = deepcopy(base_case)
        case["strategy"][0]["contracts"] = "invalid"
        return case

    @staticmethod
    def input_c59():
        case = deepcopy(base_case)
        case["strategy"][0]["contracts"] = None
        return case

    @staticmethod
    def input_c60():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_c61():
        case = deepcopy(base_case)
        case["strategy"][0]["contracts"] = -34
        return case

    @staticmethod
    def input_c62():
        case = deepcopy(base_case)
        case["strategy"][0]["contracts"] = 80.32
        return case

    @staticmethod
    def input_c63():
        case = deepcopy(base_case)
        case["strategy"][0]["contracts"] = 0
        return case


class TestSuiteCombinatorial:

    @staticmethod
    def input_ct1():
        case = deepcopy(base_case)
        return case

    @staticmethod
    def input_ct2():
        case = deepcopy(base_case)
        case["name"] = "Estratégia de validação Long Straddle – Underlying GBT – Exercise: 14,4"
        return case

    @staticmethod
    def input_ct3():
        case = deepcopy(base_case)
        case["name"] = "Estratégia de validação Long Straddle – Underlying GBT – Exercise: 14,4"
        case["username"] = "lucas_tiense_blazzi_2022"
        return case

    @staticmethod
    def input_ct4():
        case = deepcopy(base_case)
        case["name"] = "Estratégia de validação Long Straddle – Underlying GBT – Exercise: 14,4"
        case["strategy"][0]["transaction_type"] = "PUT"
        return case

    @staticmethod
    def input_ct5():
        case = deepcopy(base_case)
        case["username"] = "lucas_tiense_blazzi_2022"
        case["name"] = "Estratégia de validação Long Straddle – Underlying GBT – Exercise: 14,4"
        case["strategy"][0]["transaction_type"] = "PUT"
        return case

    @staticmethod
    def input_ct6():
        case = deepcopy(base_case)
        case["username"] = "lucas_tiense_blazzi_2022"
        return case

    @staticmethod
    def input_ct7():
        case = deepcopy(base_case)
        case["strategy"][0]["type"] = "long"
        return case

    @staticmethod
    def input_ct8():
        case = deepcopy(base_case)
        case["username"] = "lu"
        case["strategy"][0]["exercise_price"] = 0
        return case