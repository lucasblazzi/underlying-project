import json

from unittest import TestCase

import sys
sys.path.insert(0, '../app/')
import app

class TestHealth(TestCase):
    def test_lambda_handler(self):
        result = app.lambda_handler(None, None)
        expected = {
            "statusCode": 200,
            "body": json.dumps("Health Checked!")
        }
        self.assertEqual(result, expected)
    