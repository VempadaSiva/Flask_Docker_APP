import unittest
from app import app

class Test_APP(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.get_json(),{"message":"Just Started..."})

if __name__ == '__main__':
    unittest.main()
