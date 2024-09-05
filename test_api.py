# test_api.py
import unittest
from api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        #initalize test client
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/api/hello')
        data = response.get_json()

        #verify output
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Hello, CI/CD API!")

    def test_greet_name(self):
        #test dynamic api endpoint
        response = self.app.get('/api/greet/test_user')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Hello, test_user!")

if __name__ == '__main__':
    unittest.main()
