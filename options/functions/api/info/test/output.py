import pandas as pd



class TestOutput:

    @staticmethod
    def lambda_handler_output():
        _output = {
            "statusCode": 200,
            "body": '{"id": "60137665a3315885b579abe6803b55d0", "name": "BOVAA100", "type": "CALL", "exercise_price": 100.0, "currency": "R$", "expiration_date": "2022-01-21", "name_underlying": "BOVA11", "expiration_time": 0.0, "greeks": [{"name": "gamma", "value": 0.0}, {"name": "delta", "value": 1.0}, {"name": "theta", "value": 0.0}, {"name": "rho", "value": 0.0}, {"name": "gamma", "value": 0.0}, {"name": "vega", "value": 0.0}], "market": [{"name": "option_value", "value": 4.700000000000003}, {"name": "intrinsic_value", "value": 4.700000000000003}, {"name": "time_value", "value": 0.0}, {"name": "hedge_ratio", "value": 1.0}], "price": [{"name": "open_price", "value": 4.6}, {"name": "max_price", "value": 6.25}, {"name": "min_price", "value": 4.6}, {"name": "average_price", "value": 4.92}, {"name": "close_price", "value": 4.8}, {"name": "best_buy_price", "value": 4.62}, {"name": "best_sell_price", "value": 0.0}, {"name": "transactions", "value": 41.0}, {"name": "quantity", "value": 66060.0}, {"name": "volume", "value": 325120.1}], "option_close_series": [{"date": "2022-01-03", "value": 2.53}, {"date": "2022-01-04", "value": 2.15}, {"date": "2022-01-05", "value": 1.08}, {"date": "2022-01-06", "value": 0.98}, {"date": "2022-01-07", "value": 1.21}, {"date": "2022-01-10", "value": 0.91}, {"date": "2022-01-11", "value": 1.5}, {"date": "2022-01-12", "value": 2.66}, {"date": "2022-01-13", "value": 2.39}, {"date": "2022-01-14", "value": 3.23}, {"date": "2022-01-17", "value": 2.8}, {"date": "2022-01-18", "value": 2.83}, {"date": "2022-01-19", "value": 4.18}, {"date": "2022-01-20", "value": 5.02}, {"date": "2022-01-21", "value": 4.8}], "payoff": [{"exercise_price": 100.0, "name": "BOVAA100", "close_price": 4.8, "contracts": 1, "type": "CALL", "transaction_type": "SHORT", "x": [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0], "y": [4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.8, 2.8, 1.7999999999999998, 0.7999999999999998, -0.20000000000000018, -1.2000000000000002, -2.2, -3.2, -4.2, -5.2, -6.2, -7.2, -8.2, -9.2, -10.2, -11.2, -12.2, -13.2, -14.2]}, {"exercise_price": 100.0, "name": "BOVAA100", "close_price": 4.8, "contracts": 1, "type": "CALL", "transaction_type": "LONG", "x": [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0], "y": [-4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -3.8, -2.8, -1.7999999999999998, -0.7999999999999998, 0.20000000000000018, 1.2000000000000002, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2]}]}'
        }
        return _output

    @staticmethod
    def handler_output():
        _output = {
            "statusCode": 200,
            "body": '{"id": "60137665a3315885b579abe6803b55d0", "name": "BOVAA100", "type": "CALL", "exercise_price": 100.0, "currency": "R$", "expiration_date": "2022-01-21", "name_underlying": "BOVA11", "expiration_time": 0.0, "greeks": [{"name": "gamma", "value": 0.0}, {"name": "delta", "value": 1.0}, {"name": "theta", "value": 0.0}, {"name": "rho", "value": 0.0}, {"name": "gamma", "value": 0.0}, {"name": "vega", "value": 0.0}], "market": [{"name": "option_value", "value": 4.700000000000003}, {"name": "intrinsic_value", "value": 4.700000000000003}, {"name": "time_value", "value": 0.0}, {"name": "hedge_ratio", "value": 1.0}], "price": [{"name": "open_price", "value": 4.6}, {"name": "max_price", "value": 6.25}, {"name": "min_price", "value": 4.6}, {"name": "average_price", "value": 4.92}, {"name": "close_price", "value": 4.8}, {"name": "best_buy_price", "value": 4.62}, {"name": "best_sell_price", "value": 0.0}, {"name": "transactions", "value": 41.0}, {"name": "quantity", "value": 66060.0}, {"name": "volume", "value": 325120.1}], "option_close_series": [{"date": "2022-01-03", "value": 2.53}, {"date": "2022-01-04", "value": 2.15}, {"date": "2022-01-05", "value": 1.08}, {"date": "2022-01-06", "value": 0.98}, {"date": "2022-01-07", "value": 1.21}, {"date": "2022-01-10", "value": 0.91}, {"date": "2022-01-11", "value": 1.5}, {"date": "2022-01-12", "value": 2.66}, {"date": "2022-01-13", "value": 2.39}, {"date": "2022-01-14", "value": 3.23}, {"date": "2022-01-17", "value": 2.8}, {"date": "2022-01-18", "value": 2.83}, {"date": "2022-01-19", "value": 4.18}, {"date": "2022-01-20", "value": 5.02}, {"date": "2022-01-21", "value": 4.8}], "payoff": [{"exercise_price": 100.0, "name": "BOVAA100", "close_price": 4.8, "contracts": 1, "type": "CALL", "transaction_type": "SHORT", "x": [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0], "y": [4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.8, 2.8, 1.7999999999999998, 0.7999999999999998, -0.20000000000000018, -1.2000000000000002, -2.2, -3.2, -4.2, -5.2, -6.2, -7.2, -8.2, -9.2, -10.2, -11.2, -12.2, -13.2, -14.2]}, {"exercise_price": 100.0, "name": "BOVAA100", "close_price": 4.8, "contracts": 1, "type": "CALL", "transaction_type": "LONG", "x": [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0], "y": [-4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -3.8, -2.8, -1.7999999999999998, -0.7999999999999998, 0.20000000000000018, 1.2000000000000002, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2]}]}'
        }
        return _output

    @staticmethod
    def get_payoff_output():
        _output = [{'exercise_price': 100.0, 'name': 'BOVAA100', 'close_price': 4.8, 'contracts': 1, 'type': 'CALL', 'transaction_type': 'SHORT', 'x': [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0], 'y': [4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8, 3.8, 2.8, 1.7999999999999998, 0.7999999999999998, -0.20000000000000018, -1.2000000000000002, -2.2, -3.2, -4.2, -5.2, -6.2, -7.2, -8.2, -9.2, -10.2, -11.2, -12.2, -13.2, -14.2]}, {'exercise_price': 100.0, 'name': 'BOVAA100', 'close_price': 4.8, 'contracts': 1, 'type': 'CALL', 'transaction_type': 'LONG', 'x': [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0], 'y': [-4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -4.8, -3.8, -2.8, -1.7999999999999998, -0.7999999999999998, 0.20000000000000018, 1.2000000000000002, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2]}]
        return _output

    @staticmethod
    def get_option_output():
        _output = pd.DataFrame({'register_type': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1}, 'date': {0: '2022-01-03', 1: '2022-01-04', 2: '2022-01-05', 3: '2022-01-06', 4: '2022-01-07', 5: '2022-01-10', 6: '2022-01-11', 7: '2022-01-12', 8: '2022-01-13', 9: '2022-01-14', 10: '2022-01-17', 11: '2022-01-18', 12: '2022-01-19', 13: '2022-01-20', 14: '2022-01-21'}, 'name': {0: 'BOVAA100', 1: 'BOVAA100', 2: 'BOVAA100', 3: 'BOVAA100', 4: 'BOVAA100', 5: 'BOVAA100', 6: 'BOVAA100', 7: 'BOVAA100', 8: 'BOVAA100', 9: 'BOVAA100', 10: 'BOVAA100', 11: 'BOVAA100', 12: 'BOVAA100', 13: 'BOVAA100', 14: 'BOVAA100'}, 'company': {0: 'BOVA  FM', 1: 'BOVA  FM', 2: 'BOVA  FM', 3: 'BOVA  FM', 4: 'BOVA  FM', 5: 'BOVA  FM', 6: 'BOVA  FM', 7: 'BOVA  FM', 8: 'BOVA  FM', 9: 'BOVA  FM', 10: 'BOVA', 11: 'BOVA', 12: 'BOVA', 13: 'BOVA', 14: 'BOVA'}, 'share_type': {0: 'CI', 1: 'CI', 2: 'CI', 3: 'CI', 4: 'CI', 5: 'CI', 6: 'CI', 7: 'CI', 8: 'CI', 9: 'CI', 10: 'CI', 11: 'CI', 12: 'CI', 13: 'CI', 14: 'CI'}, 'forward_market_deadline': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0}, 'currency': {0: 'R$', 1: 'R$', 2: 'R$', 3: 'R$', 4: 'R$', 5: 'R$', 6: 'R$', 7: 'R$', 8: 'R$', 9: 'R$', 10: 'R$', 11: 'R$', 12: 'R$', 13: 'R$', 14: 'R$'}, 'open_price': {0: 3.6, 1: 2.6, 2: 2.0, 3: 1.13, 4: 1.1, 5: 0.9, 6: 0.91, 7: 1.55, 8: 2.32, 9: 2.34, 10: 2.95, 11: 2.57, 12: 3.42, 13: 4.5, 14: 4.6}, 'max_price': {0: 3.99, 1: 2.6, 2: 2.0, 3: 1.4, 4: 1.24, 5: 1.18, 6: 1.5, 7: 2.72, 8: 2.92, 9: 3.38, 10: 3.18, 11: 3.38, 12: 5.6, 13: 6.0, 14: 6.25}, 'min_price': {0: 2.37, 1: 2.01, 2: 1.04, 3: 0.95, 4: 0.84, 5: 0.77, 6: 0.83, 7: 1.55, 8: 2.06, 9: 2.01, 10: 2.52, 11: 2.18, 12: 3.42, 13: 4.5, 14: 4.6}, 'average_price': {0: 2.77, 1: 2.26, 2: 1.5, 3: 1.15, 4: 1.02, 5: 0.88, 6: 1.18, 7: 2.22, 8: 2.47, 9: 2.59, 10: 2.93, 11: 2.68, 12: 4.5, 13: 5.39, 14: 4.92}, 'close_price': {0: 2.53, 1: 2.15, 2: 1.08, 3: 0.98, 4: 1.21, 5: 0.91, 6: 1.5, 7: 2.66, 8: 2.39, 9: 3.23, 10: 2.8, 11: 2.83, 12: 4.18, 13: 5.02, 14: 4.8}, 'best_buy_price': {0: 2.49, 1: 2.04, 2: 1.05, 3: 0.9, 4: 1.12, 5: 0.91, 6: 1.3, 7: 2.31, 8: 2.39, 9: 3.23, 10: 2.57, 11: 2.68, 12: 4.13, 13: 4.93, 14: 4.62}, 'best_sell_price': {0: 2.6, 1: 2.16, 2: 1.08, 3: 1.0, 4: 1.21, 5: 0.95, 6: 1.51, 7: 2.73, 8: 2.81, 9: 3.42, 10: 3.18, 11: 3.38, 12: 4.52, 13: 5.3, 14: 0.0}, 'transactions': {0: 917.0, 1: 918.0, 2: 720.0, 3: 547.0, 4: 1788.0, 5: 833.0, 6: 966.0, 7: 789.0, 8: 534.0, 9: 178.0, 10: 821.0, 11: 69.0, 12: 143.0, 13: 175.0, 14: 41.0}, 'quantity': {0: 620590.0, 1: 273560.0, 2: 1358710.0, 3: 958840.0, 4: 510530.0, 5: 1366570.0, 6: 718340.0, 7: 469290.0, 8: 332670.0, 9: 152460.0, 10: 60190.0, 11: 74630.0, 12: 125980.0, 13: 82960.0, 14: 66060.0}, 'volume': {0: 1724207.0, 1: 618424.9, 2: 2042720.8, 3: 1109467.7, 4: 525635.4, 5: 1213407.6, 6: 848050.1, 7: 1043209.0, 8: 822089.8, 9: 395779.8, 10: 176901.1, 11: 200190.8, 12: 567715.1, 13: 447929.7, 14: 325120.1}, 'exercise_price': {0: 100.0, 1: 100.0, 2: 100.0, 3: 100.0, 4: 100.0, 5: 100.0, 6: 100.0, 7: 100.0, 8: 100.0, 9: 100.0, 10: 100.0, 11: 100.0, 12: 100.0, 13: 100.0, 14: 100.0}, 'price_correction_indicator': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0}, 'expiration_date': {0: '2022-01-21', 1: '2022-01-21', 2: '2022-01-21', 3: '2022-01-21', 4: '2022-01-21', 5: '2022-01-21', 6: '2022-01-21', 7: '2022-01-21', 8: '2022-01-21', 9: '2022-01-21', 10: '2022-01-21', 11: '2022-01-21', 12: '2022-01-21', 13: '2022-01-21', 14: '2022-01-21'}, 'price_factor': {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 1.0, 14: 1.0}, 'exercise_price_points': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0}, 'isin_code': {0: 'BRBOVACTF003', 1: 'BRBOVACTF003', 2: 'BRBOVACTF003', 3: 'BRBOVACTF003', 4: 'BRBOVACTF003', 5: 'BRBOVACTF003', 6: 'BRBOVACTF003', 7: 'BRBOVACTF003', 8: 'BRBOVACTF003', 9: 'BRBOVACTF003', 10: 'BRBOVACTF003', 11: 'BRBOVACTF003', 12: 'BRBOVACTF003', 13: 'BRBOVACTF003', 14: 'BRBOVACTF003'}, 'distribution_share_number': {0: 105.0, 1: 105.0, 2: 105.0, 3: 105.0, 4: 105.0, 5: 105.0, 6: 105.0, 7: 105.0, 8: 105.0, 9: 105.0, 10: 105.0, 11: 105.0, 12: 105.0, 13: 105.0, 14: 105.0}, 'type': {0: 'CALL', 1: 'CALL', 2: 'CALL', 3: 'CALL', 4: 'CALL', 5: 'CALL', 6: 'CALL', 7: 'CALL', 8: 'CALL', 9: 'CALL', 10: 'CALL', 11: 'CALL', 12: 'CALL', 13: 'CALL', 14: 'CALL'}, 'folder': {0: 'opcoes', 1: 'opcoes', 2: 'opcoes', 3: 'opcoes', 4: 'opcoes', 5: 'opcoes', 6: 'opcoes', 7: 'opcoes', 8: 'opcoes', 9: 'opcoes', 10: 'opcoes', 11: 'opcoes', 12: 'opcoes', 13: 'opcoes', 14: 'opcoes'}, 'id': {0: '60137665a3315885b579abe6803b55d0', 1: '60137665a3315885b579abe6803b55d0', 2: '60137665a3315885b579abe6803b55d0', 3: '60137665a3315885b579abe6803b55d0', 4: '60137665a3315885b579abe6803b55d0', 5: '60137665a3315885b579abe6803b55d0', 6: '60137665a3315885b579abe6803b55d0', 7: '60137665a3315885b579abe6803b55d0', 8: '60137665a3315885b579abe6803b55d0', 9: '60137665a3315885b579abe6803b55d0', 10: '60137665a3315885b579abe6803b55d0', 11: '60137665a3315885b579abe6803b55d0', 12: '60137665a3315885b579abe6803b55d0', 13: '60137665a3315885b579abe6803b55d0', 14: '60137665a3315885b579abe6803b55d0'}, 'name_underlying': {0: 'BOVA11', 1: 'BOVA11', 2: 'BOVA11', 3: 'BOVA11', 4: 'BOVA11', 5: 'BOVA11', 6: 'BOVA11', 7: 'BOVA11', 8: 'BOVA11', 9: 'BOVA11', 10: 'BOVA11', 11: 'BOVA11', 12: 'BOVA11', 13: 'BOVA11', 14: 'BOVA11'}, 'company_underlying': {0: 'ISHARES BOVA', 1: 'ISHARES BOVA', 2: 'ISHARES BOVA', 3: 'ISHARES BOVA', 4: 'ISHARES BOVA', 5: 'ISHARES BOVA', 6: 'ISHARES BOVA', 7: 'ISHARES BOVA', 8: 'ISHARES BOVA', 9: 'ISHARES BOVA', 10: 'ISHARES BOVA', 11: 'ISHARES BOVA', 12: 'ISHARES BOVA', 13: 'ISHARES BOVA', 14: 'ISHARES BOVA'}, 'close_price_underlying': {0: 99.93, 1: 99.57, 2: 97.1, 3: 97.85, 4: 98.7, 5: 98.43, 6: 100.1, 7: 101.91, 8: 101.55, 9: 103.07, 10: 102.58, 11: 102.85, 12: 104.05, 13: 104.9, 14: 104.7}, 'expiration_time': {0: 0.049315068493150684, 1: 0.04657534246575343, 2: 0.043835616438356165, 3: 0.0410958904109589, 4: 0.038356164383561646, 5: 0.030136986301369864, 6: 0.0273972602739726, 7: 0.024657534246575342, 8: 0.021917808219178082, 9: 0.019178082191780823, 10: 0.010958904109589041, 11: 0.00821917808219178, 12: 0.005479452054794521, 13: 0.0027397260273972603, 14: 0.0}, 'return_underlying': {0: 0.0, 1: -0.003602521765235789, 2: -0.02480666867530379, 3: 0.007723995880535517, 4: 0.008686765457332823, 5: -0.0027355623100303594, 6: 0.01696637204104423, 7: 0.018081918081918058, 8: -0.0035325287017956564, 9: 0.01496799606105359, 10: -0.00475405064519252, 11: 0.002632092025735888, 12: 0.011667476908118646, 13: 0.00816914944738123, 14: -0.0019065776930410339}, 'volatility_underlying': {0: 0.175315602666898, 1: 0.175315602666898, 2: 0.175315602666898, 3: 0.175315602666898, 4: 0.175315602666898, 5: 0.175315602666898, 6: 0.175315602666898, 7: 0.175315602666898, 8: 0.175315602666898, 9: 0.175315602666898, 10: 0.175315602666898, 11: 0.175315602666898, 12: 0.175315602666898, 13: 0.175315602666898, 14: 0.175315602666898}, 'n1': {0: -0.0007002451143933149, 1: -0.004309271588098514, 2: -0.029428810690812168, 3: -0.021734492146006208, 4: -0.01308523954865548, 5: -0.015824550346971347, 6: 0.0009995003330834232, 7: 0.018919884852510768, 8: 0.015381102038302391, 9: 0.030238183060609946, 10: 0.02547279597303107, 11: 0.02810143011087478, 12: 0.039701366851552046, 13: 0.04783732941416027, 14: 0.045928931888399735}, 'n2': {0: 0.0027304658762907367, 1: 0.002578773327607918, 2: 0.002427080778925099, 3: 0.0022753882302422803, 4: 0.0021236956815594617, 5: 0.0016686180355110058, 6: 0.0015169254868281868, 7: 0.0013652329381453683, 8: 0.0012135403894625496, 9: 0.0010618478407797309, 10: 0.0006067701947312748, 11: 0.00045507764604845607, 12: 0.0003033850973656374, 13: 0.0001516925486828187, 14: 0.0}, 'd': {0: 0.03893232940795373, 1: 0.0378354233220082, 2: 0.03670575217567003, 3: 0.03554019172159668, 4: 0.03433508719129736, 5: 0.03043480190361722, 6: 0.029018445026199557, 7: 0.02752931413175252, 8: 0.025954886271969152, 9: 0.024278572985597734, 10: 0.018352876087835014, 11: 0.01589405692457309, 12: 0.012977443135984576, 13: 0.009176438043917507, 14: 0.0}, 'd1': {0: 0.05214742587384601, 1: -0.04573751549606677, 2: -0.735626660983802, 3: -0.5475238869895919, 4: -0.319251959548667, 5: -0.46512319535675667, 6: 0.08671814832392408, 7: 0.7368551825727879, 8: 0.6393648677122843, 9: 1.2892038967840957, 10: 1.4210070423266725, 11: 1.7966783365909114, 12: 3.082637429401658, 13: 5.229591452933313, 14: 0.0}, 'd2': {0: 0.013215096465892279, 1: -0.08357293881807497, 2: -0.7723324131594721, 3: -0.5830640787111886, 4: -0.35358704673996433, 5: -0.49555799726037386, 6: 0.05769970329772452, 7: 0.7093258684410354, 8: 0.6134099814403151, 9: 1.264925323798498, 10: 1.4026541662388374, 11: 1.7807842796663382, 12: 3.0696599862656733, 13: 5.2204150148893955, 14: 0.0}, 'normal_d1': {0: 0.5207943880178763, 1: 0.48175973102127356, 2: 0.23097896641596538, 3: 0.29200943214826847, 4: 0.37476772935351843, 5: 0.3209216180691128, 6: 0.5345522247580189, 7: 0.7693947894635795, 8: 0.7387072008149876, 9: 0.9013363946668557, 10: 0.9223426439275241, 11: 0.9638066499714963, 12: 0.9989741251604363, 13: 0.9999999150574767, 14: 1.0}, 'normal_d2': {0: 0.5052719072728103, 1: 0.4666979916706648, 2: 0.21995878629305432, 3: 0.27992508211743194, 4: 0.3618241916233361, 5: 0.3101031466913986, 6: 0.5230060849808775, 7: 0.7609388604723633, 8: 0.7301973560943975, 9: 0.8970509507578651, 10: 0.9196400044600137, 11: 0.9625261507312789, 12: 0.9989284870373429, 13: 0.999999910738692, 14: 1.0}, 'a': {0: 52.04298319462638, 1: 47.968816417788204, 2: 22.428057638990236, 3: 28.573122935708067, 4: 36.98957488719227, 5: 31.588314866542774, 6: 53.50867769827769, 7: 78.40902299423338, 8: 75.015716242762, 9: 92.90074219831281, 10: 94.61390841408542, 11: 99.1275139495684, 12: 103.94325772294339, 13: 104.89999108952931, 14: 104.7}, 'b': {0: 50.42761889254625, 1: 46.58293363287054, 2: 21.957344306741156, 3: 27.946530929651512, 4: 36.1269489730012, 5: 30.97295489474885, 6: 52.24332415716044, 7: 76.01887154272514, 8: 72.95574636116771, 9: 89.63630659632676, 10: 91.92369629393663, 11: 96.22097557905909, 12: 99.87095677993331, 13: 99.98903277120372, 14: 100.0}, 'option_value': {0: 1.6153643020801312, 1: 1.385882784917662, 2: 0.47071333224907974, 3: 0.6265920060565549, 4: 0.8626259141910708, 5: 0.6153599717939251, 6: 1.2653535411172498, 7: 2.3901514515082454, 8: 2.0599698815942844, 9: 3.264435601986051, 10: 2.690212120148786, 11: 2.9065383705093097, 12: 4.072300943010077, 13: 4.910958318325584, 14: 4.700000000000003}, 'intrinsic_value': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.09999999999999432, 7: 1.9099999999999966, 8: 1.5499999999999972, 9: 3.069999999999993, 10: 2.5799999999999983, 11: 2.8499999999999943, 12: 4.049999999999997, 13: 4.900000000000006, 14: 4.700000000000003}, 'time_value': {0: 1.6153643020801312, 1: 1.385882784917662, 2: 0.47071333224907974, 3: 0.6265920060565549, 4: 0.8626259141910708, 5: 0.6153599717939251, 6: 1.1653535411172555, 7: 0.4801514515082488, 8: 0.5099698815942872, 9: 0.1944356019860578, 10: 0.11021212014878756, 11: 0.05653837050931543, 12: 0.022300943010080232, 13: 0.01095831832557792, 14: 0.0}, 'delta': {0: 0.5207943880178763, 1: 0.48175973102127356, 2: 0.23097896641596538, 3: 0.29200943214826847, 4: 0.37476772935351843, 5: 0.3209216180691128, 6: 0.5345522247580189, 7: 0.7693947894635795, 8: 0.7387072008149876, 9: 0.9013363946668557, 10: 0.9223426439275241, 11: 0.9638066499714963, 12: 0.9989741251604363, 13: 0.9999999150574767, 14: 1.0}, 'theta': {0: -0.04858128941399064, 1: -0.04926243032648498, 2: -0.036306694857452616, 3: -0.04287082841457864, 4: -0.04984460001605484, 5: -0.052148021619768975, 6: -0.06344915105830967, 7: -0.05572757310906756, 8: -0.061565203491235, 9: -0.0408850993157011, 10: -0.044280432783796696, 11: -0.032183658630707275, 12: -0.012108369318745489, 13: -0.010957923353122696, 14: 0.0}, 'rho': {0: 0.024868414796324175, 1: 0.021696160870104085, 2: 0.009625137230352288, 3: 0.011484875724514319, 4: 0.013856911934849775, 5: 0.009334315173759928, 6: 0.014313239495112446, 7: 0.01874437928450757, 8: 0.015990300572310732, 9: 0.0171905245527202, 10: 0.01007382973084237, 11: 0.00790857333526513, 12: 0.005472381193421003, 13: 0.002739425555375444, 14: 0.0}, 'gamma': {0: 0.10240314358785273, 1: 0.10578612439934018, 2: 0.08539810232052356, 3: 0.09874896377055618, 4: 0.11187233890452378, 5: 0.1195183412190663, 6: 0.13682608360304005, 7: 0.10839183556661088, 8: 0.12337976661320135, 9: 0.06944576725916461, 10: 0.07720870721090294, 11: 0.04858566968843822, 12: 0.0025527239491189937, 13: 4.772891865675415e-07, 14: 0.0}, 'vega': {0: 0.08841079042337438, 1: 0.08563717782679321, 2: 0.06187772914067579, 3: 0.06811976963113363, 4: 0.0732846070416141, 5: 0.06118006258021189, 6: 0.06585136106789172, 7: 0.04866316909100986, 8: 0.048890163695801535, 9: 0.024804819843919274, 10: 0.015609154020568188, 11: 0.007405693681971237, 12: 0.00026548850511938786, 13: 2.522669032910341e-08, 14: 0.0}, 'hedge_ratio': {0: 1.9201435787470027, 1: 2.075723510306929, 2: 4.329398540121268, 3: 3.4245469149511845, 4: 2.668319392720978, 5: 3.1160256701206173, 6: 1.8707246059123221, 7: 1.2997228648990435, 8: 1.3537163288739271, 9: 1.1094636873834565, 10: 1.084195777549431, 11: 1.0375525008356956, 12: 1.0010269283395092, 13: 1.0000000849425306, 14: 1.0}})
        return _output

    @staticmethod
    def preprocess_payload_output():
        _output = {'options': [{'exercise_price': 100.0, 'name': 'BOVAA100', 'close_price': 4.8, 'contracts': 1, 'type': 'CALL', 'transaction_type': 'SHORT'}, {'exercise_price': 100.0, 'name': 'BOVAA100', 'close_price': 4.8, 'contracts': 1, 'type': 'CALL', 'transaction_type': 'LONG'}], 'strategy': False}
        return _output