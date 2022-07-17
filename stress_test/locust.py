from locust import HttpUser, task
import json


class UserBehavior(HttpUser):

    @task
    def create_payoff_post(self):
        headers = {"content-type": "application/json"}
        self.client.post("/v1/payoff", data=json.dumps(
            {
                "strategy": [
                    {
                        "name": "custom",
                        "exercise_price": 12.32,
                        "transaction_type": "LONG",
                        "close_price": 1.23,
                        "contracts": 1,
                        "type": "PUT"
                    },
                    {
                        "name": "custom",
                        "exercise_price": 12.32,
                        "transaction_type": "SHORT",
                        "close_price": 1.23,
                        "contracts": 1,
                        "type": "CAll"
                    }
                ]
            }),
            headers=headers,
            name="Payoff Request")
