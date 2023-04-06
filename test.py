import unittest
import sys

sys.path.insert(0, '/usr/bin/python3.6/site-packages')
from app import app


class TestApp(unittest.TestCase):
    
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertIn(I am almost DevOps Engineer!', response.data)


if __name__ == '__main__':
    unittest.main()
