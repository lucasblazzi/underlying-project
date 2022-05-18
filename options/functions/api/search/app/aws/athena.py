import os

from aiobotocore.session import get_session

ACCOUNT_ID = os.environ.get("ACCOUNT_ID", "182960656850")
REGION = os.environ.get("REGION", "us-east-1")
ATHENA_DB = os.environ.get("ATHENA_DB", "db_underlying")


class Athena:
    def __init__(self):
        self.session = get_session()

    @staticmethod
    def build_parameters(query):
        return {
            "region": REGION,
            "database": ATHENA_DB,
            "bucket": f"aws-athena-query-results-{ACCOUNT_ID}-{REGION}",
            "path": "",
            "query": query
        }

    @staticmethod
    def get_results(data):
        return [obj["VarCharValue"] if obj else "-" for obj in data["Data"]]

    def build_results(self, result_data):
        raw_header = result_data["Rows"][0]
        rows = result_data["Rows"][1:]
        header = [obj["VarCharValue"] for obj in raw_header["Data"]]
        return [dict(zip(header, self.get_results(row))) for row in rows]

    async def run_query(self, query, client):
        result = dict()
        result[query] = {"result": []}
        params = self.build_parameters(query)
        response_query_execution_id = await client.start_query_execution(
            QueryString=params["query"],
            QueryExecutionContext={
                'Database': params["database"]
            },
            ResultConfiguration={
                'OutputLocation': 's3://' + params["bucket"] + '/' + params["path"]
            }
        )
        status = "RUNNING"

        while status in ("RUNNING", "QUEUED"):
            print(status)
            response_get_query_details = await client.get_query_execution(
                QueryExecutionId=response_query_execution_id["QueryExecutionId"])

            status = response_get_query_details["QueryExecution"]["Status"]["State"]

            if (status == "FAILED") or (status == "CANCELLED"):
                raise FileNotFoundError

            elif status == 'SUCCEEDED':
                result[query]["location"] = response_get_query_details["QueryExecution"] \
                    ["ResultConfiguration"]["OutputLocation"]

                response_query_result = await client.get_query_results(
                    QueryExecutionId=response_query_execution_id['QueryExecutionId']
                )
                result_data = response_query_result['ResultSet']

                if len(result_data["Rows"]) > 1:
                    result[query]["result"] = self.build_results(result_data)

        return result
