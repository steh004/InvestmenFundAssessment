import unittest
from InvestmentFundsAPI import app
import requests
import sqlite3

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'
        # Connect to the SQLite database
        self.conn = sqlite3.connect('invesmentfunds.db')
        self.c = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_get_funds(self):
        response = requests.get(f'{self.base_url}/funds')
        self.assertEqual(response.status_code, 200)
        # Verify that the response contains a list of funds
        self.assertTrue(isinstance(response.json(), list))

    def test_create_fund(self):
        data = {
            "fund_id" : "42qf3q",
            "fund_name": "Test Fund",
            "fund_manager_name": "John Doe",
            "fund_description": "A test fund",
            "fund_nav": 1000000,
            "creation_date": "2024-04-30",
            "performance": 5
        }
        response = requests.post(f'{self.base_url}/addfunds', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_fund(self):
        response = requests.get(f'{self.base_url}/funds/4f2w13')
        self.assertEqual(response.status_code, 200)
        # Verify that the response contains the correct fund details
        self.assertEqual(response.json()['fund_id'], "4f2w13")

    def test_update_performance(self):
        data = {
            "performance": 7
        }
        response = requests.put(f'{self.base_url}/funds/12fq52', json=data)
        self.assertEqual(response.status_code, 200)
        # Verify that the performance is updated in the database
        self.c.execute('SELECT performance FROM funds WHERE fund_id = ?', ("12fq52",))
        performance = self.c.fetchone()[0]
        self.assertEqual(performance, 7)

    def test_delete_fund(self):
        response = requests.delete(f'{self.base_url}/funds/8d2gh2')
        self.assertEqual(response.status_code, 200)
        # Verify that the fund is deleted from the database
        self.c.execute('SELECT * FROM funds WHERE fund_id = ?', ("8d2gh2",))
        self.assertIsNone(self.c.fetchone())

if __name__ == '__main__':
    unittest.main()