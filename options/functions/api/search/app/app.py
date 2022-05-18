import os
import json
import asyncio
from html import escape

from .aws.athena import Athena


REGION = os.environ.get("REGION", "us-east-1")
ATHENA_DB = os.environ.get("ATHENA_DB", "db_underlying")
OPTIONS_TABLE = os.environ.get("OPTIONS_TABLE", "tb_options_series")

mock = [
  {
    "id": "60e28275f368b250d90f5e7d4ff1bf6e",
    "max_date": "2022-12-09",
    "date": "2022-12-09",
    "company": "PETRE",
    "currency": "R$",
    "open_price": "1.03",
    "max_price": "1.07",
    "min_price": "1.02",
    "average_price": "1.05",
    "close_price": "1.07",
    "transactions": "51.0",
    "quantity": "90800.0",
    "volume": "95635.0",
    "exercise_price": "33.34",
    "expiration_date": "2023-09-24",
    "isin_code": "BRPETRACNPR6",
    "type": "CALL",
    "name_underlying": "PETR4",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "30.26",
    "expiration_time": "0.2136986301369863",
    "option_value": "0.8409015758654892",
    "intrinsic_value": "0.0",
    "time_value": "0.8409015758654892",
    "delta": "0.3075566384876728",
    "theta": "-0.011335998545157782",
    "rho": "0.01809121807595003",
    "gamma": "0.0761255134632668",
    "vega": "0.049179707012786796",
    "hedge_ratio": "3.251433638100714",
    "name": "PETRG349"
  },
  {
    "id": "415ce955746abc93dd3f4ecb8e468d4d",
    "max_date": "2022-10-10",
    "date": "2022-10-10",
    "company": "PETR",
    "currency": "R$",
    "open_price": "10.5",
    "max_price": "11.01",
    "min_price": "9.81",
    "average_price": "10.13",
    "close_price": "10.12",
    "transactions": "24.0",
    "quantity": "21400.0",
    "volume": "216808.0",
    "exercise_price": "24.51",
    "expiration_date": "2023-08-16",
    "isin_code": "BRPETRACNPR6",
    "type": "CALL",
    "name_underlying": "PETR4",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "33.87",
    "expiration_time": "0.2136986301369863",
    "option_value": "9.607384175896147",
    "intrinsic_value": "9.359999999999996",
    "time_value": "0.24738417589615125",
    "delta": "0.9819096339360638",
    "theta": "-0.004184176515990347",
    "rho": "0.05053950191206657",
    "gamma": "0.007956304770043388",
    "vega": "0.006960831721320836",
    "hedge_ratio": "1.0184236567589418",
    "name": "PETRD291"
  },
  {
    "id": "6fc2b000e7995631f18f3bf504efa31b",
    "max_date": "2022-08-11",
    "date": "2022-08-11",
    "company": "PETR",
    "currency": "R$",
    "open_price": "4.65",
    "max_price": "4.65",
    "min_price": "4.65",
    "average_price": "4.65",
    "close_price": "4.65",
    "transactions": "1.0",
    "quantity": "1500.0",
    "volume": "6975.0",
    "exercise_price": "31.16",
    "expiration_date": "2023-02-27",
    "isin_code": "BRPETRACNOR9",
    "type": "CALL",
    "name_underlying": "PETR3",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "35.8",
    "expiration_time": "0.14246575342465753",
    "option_value": "5.130819800027627",
    "intrinsic_value": "4.639999999999997",
    "time_value": "0.49081980002763004",
    "delta": "0.8751094679822857",
    "theta": "-0.012309867679647798",
    "rho": "0.03732331934231195",
    "gamma": "0.0431154482209357",
    "vega": "0.027799102340385375",
    "hedge_ratio": "1.1427141821533147",
    "name": "PETRC311"
  },
  {
    "id": "3adc313652c7bd61cf418058834cd159",
    "max_date": "2022-10-29",
    "date": "2022-10-29",
    "company": "PETRE",
    "currency": "R$",
    "open_price": "3.1",
    "max_price": "3.1",
    "min_price": "3.1",
    "average_price": "3.1",
    "close_price": "3.1",
    "transactions": "1.0",
    "quantity": "100.0",
    "volume": "310.0",
    "exercise_price": "33.01",
    "expiration_date": "2023-02-25",
    "isin_code": "BRPETRACNPR6",
    "type": "PUT",
    "name_underlying": "PETR4",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "30.83",
    "expiration_time": "0.2547945205479452",
    "option_value": "3.6875506511280243",
    "intrinsic_value": "2.1799999999999997",
    "time_value": "1.5075506511280246",
    "delta": "-0.5676812595274692",
    "theta": "-0.011412076515402308",
    "rho": "-0.053988828522177276",
    "gamma": "0.060517834294372026",
    "vega": "0.06118825143087288",
    "hedge_ratio": "-1.761551897683548",
    "name": "PETRR330"
  },
  {
    "id": "cf24caad6a49bbd345720492c83bdc07",
    "max_date": "2022-07-18",
    "date": "2022-07-18",
    "company": "PETRE",
    "currency": "R$",
    "open_price": "8.17",
    "max_price": "8.17",
    "min_price": "7.83",
    "average_price": "8.08",
    "close_price": "8.13",
    "transactions": "33.0",
    "quantity": "14300.0",
    "volume": "115575.0",
    "exercise_price": "21.84",
    "expiration_date": "2023-07-09",
    "isin_code": "BRPETRACNPR6",
    "type": "CALL",
    "name_underlying": "PETR4",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "29.98",
    "expiration_time": "0.049315068493150684",
    "option_value": "8.183388602913539",
    "intrinsic_value": "8.14",
    "time_value": "0.043388602913537966",
    "delta": "0.9995539289377752",
    "theta": "-0.002516849417964709",
    "rho": "0.010742418831768146",
    "gamma": "5.477437570072151E-4",
    "vega": "1.0644853623850916E-4",
    "hedge_ratio": "1.000446270130416",
    "name": "PETRE191"
  },
  {
    "id": "5f48107b2c140308319ec37be0dd7579",
    "max_date": "2022-01-01",
    "date": "2022-01-01",
    "company": "PETRE",
    "currency": "R$",
    "open_price": "0.16",
    "max_price": "0.16",
    "min_price": "0.14",
    "average_price": "0.15",
    "close_price": "0.14",
    "transactions": "111.0",
    "quantity": "388800.0",
    "volume": "59632.0",
    "exercise_price": "26.76",
    "expiration_date": "2022-07-31",
    "isin_code": "BRPETRACNPR6",
    "type": "PUT",
    "name_underlying": "PETR4",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "31.77",
    "expiration_time": "0.07671232876712329",
    "option_value": "0.017168411785526416",
    "intrinsic_value": "0.0",
    "time_value": "0.017168411785526416",
    "delta": "-0.017276708964555205",
    "theta": "-0.0019830336611851743",
    "rho": "-4.342297193562869E-4",
    "gamma": "0.015954532456074488",
    "vega": "0.003761313802699807",
    "hedge_ratio": "-57.88139408099043",
    "name": "PETRN298"
  },
  {
    "id": "778f945ed37a24d85a8e160ff1addef8",
    "max_date": "2022-08-08",
    "date": "2022-08-08",
    "company": "PETRE",
    "currency": "R$",
    "open_price": "2.83",
    "max_price": "2.83",
    "min_price": "2.77",
    "average_price": "2.77",
    "close_price": "2.8",
    "transactions": "5.0",
    "quantity": "17600.0",
    "volume": "48918.0",
    "exercise_price": "30.0",
    "expiration_date": "2023-11-12",
    "isin_code": "BRPETRACNPR6",
    "type": "PUT",
    "name_underlying": "PETR4",
    "company_underlying": "PETROBRAS",
    "close_price_underlying": "32.35",
    "expiration_time": "1.8712328767123287",
    "option_value": "3.7920155856193443",
    "intrinsic_value": "0.0",
    "time_value": "3.7920155856193443",
    "delta": "-0.2904220209381323",
    "theta": "-0.002499501969900399",
    "rho": "-0.24676262243033129",
    "gamma": "0.021774809353456617",
    "vega": "0.15158147612653164",
    "hedge_ratio": "-3.4432650691216935",
    "name": "PETRX300"
  }
]


async def run_queries(event):
    athena = Athena()
    _input = escape(event["query"])
    query = f"""
        SELECT *
        FROM (
              SELECT id, MAX(date) as max_date
              FROM {ATHENA_DB}.{OPTIONS_TABLE}
              GROUP BY id, date
        ) r
        INNER JOIN {ATHENA_DB}.{OPTIONS_TABLE} t
        ON t.id = r.id AND t.date = r.max_date
        WHERE name LIKE '{_input}%'
        LIMIT 10
    """
    async with athena.session.create_client("athena", region_name=REGION) as athena_client:
        result = await athena.run_query(query, athena_client)
    return result.get(query, {}).get("result", [])


async def handler(event):
    # results = await run_queries(event)
    return {
        "statusCode": 200,
        "body": json.dumps(mock)
    }


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handler(event))
