import unittest
from main import app
class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_register(self):
        rv = self.app.get('/register')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Done\n')
if __name__ == '__main__':
    unittest.main()
