

class TestInput:

    @staticmethod
    def lambda_handler_input():
        _input = {
            "event": {
                "body": '{"id": "60137665a3315885b579abe6803b55d0", "name": "BOVAA100"}'
            },
            "context": None
        }
        return _input

    @staticmethod
    def handler_input():
        _input = {
            "event": {
                "body": '{"id": "60137665a3315885b579abe6803b55d0", "name": "BOVAA100"}'
            }
        }
        return _input

    @staticmethod
    def get_payoff_input():
        _input = {
            "option": {'register_type': 1, 'date': '2022-01-21', 'name': 'BOVAA100', 'company': 'BOVA', 'share_type': 'CI', 'forward_market_deadline': 0.0, 'currency': 'R$', 'open_price': 4.6, 'max_price': 6.25, 'min_price': 4.6, 'average_price': 4.92, 'close_price': 4.8, 'best_buy_price': 4.62, 'best_sell_price': 0.0, 'transactions': 41.0, 'quantity': 66060.0, 'volume': 325120.1, 'exercise_price': 100.0, 'price_correction_indicator': 0.0, 'expiration_date': '2022-01-21', 'price_factor': 1.0, 'exercise_price_points': 0.0, 'isin_code': 'BRBOVACTF003', 'distribution_share_number': 105.0, 'type': 'CALL', 'folder': 'opcoes', 'id': '60137665a3315885b579abe6803b55d0', 'name_underlying': 'BOVA11', 'company_underlying': 'ISHARES BOVA', 'close_price_underlying': 104.7, 'expiration_time': 0.0, 'return_underlying': -0.0019065776930410339, 'volatility_underlying': 0.175315602666898, 'n1': 0.045928931888399735, 'n2': 0.0, 'd': 0.0, 'd1': 0.0, 'd2': 0.0, 'normal_d1': 1.0, 'normal_d2': 1.0, 'a': 104.7, 'b': 100.0, 'option_value': 4.700000000000003, 'intrinsic_value': 4.700000000000003, 'time_value': 0.0, 'delta': 1.0, 'theta': 0.0, 'rho': 0.0, 'gamma': 0.0, 'vega': 0.0, 'hedge_ratio': 1.0}
        }
        return _input

    @staticmethod
    def get_option_input():
        _input = {
            "option": {'id': '60137665a3315885b579abe6803b55d0', 'name': 'BOVAA100'}
        }
        return _input

    @staticmethod
    def preprocess_payload_input():
        _input = {
            "option": {'register_type': 1, 'date': '2022-01-21', 'name': 'BOVAA100', 'company': 'BOVA', 'share_type': 'CI', 'forward_market_deadline': 0.0, 'currency': 'R$', 'open_price': 4.6, 'max_price': 6.25, 'min_price': 4.6, 'average_price': 4.92, 'close_price': 4.8, 'best_buy_price': 4.62, 'best_sell_price': 0.0, 'transactions': 41.0, 'quantity': 66060.0, 'volume': 325120.1, 'exercise_price': 100.0, 'price_correction_indicator': 0.0, 'expiration_date': '2022-01-21', 'price_factor': 1.0, 'exercise_price_points': 0.0, 'isin_code': 'BRBOVACTF003', 'distribution_share_number': 105.0, 'type': 'CALL', 'folder': 'opcoes', 'id': '60137665a3315885b579abe6803b55d0', 'name_underlying': 'BOVA11', 'company_underlying': 'ISHARES BOVA', 'close_price_underlying': 104.7, 'expiration_time': 0.0, 'return_underlying': -0.0019065776930410339, 'volatility_underlying': 0.175315602666898, 'n1': 0.045928931888399735, 'n2': 0.0, 'd': 0.0, 'd1': 0.0, 'd2': 0.0, 'normal_d1': 1.0, 'normal_d2': 1.0, 'a': 104.7, 'b': 100.0, 'option_value': 4.700000000000003, 'intrinsic_value': 4.700000000000003, 'time_value': 0.0, 'delta': 1.0, 'theta': 0.0, 'rho': 0.0, 'gamma': 0.0, 'vega': 0.0, 'hedge_ratio': 1.0}
        }
        return _input
