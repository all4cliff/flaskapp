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
        self.assertIn(b'Hello there! I am almost DevOps Engineer in the making, and I am excited to use Flask to build some awesome web applications. Stay tuned for some amazing projects coming soon!', response.data)


if __name__ == '__main__':
    unittest.main()
