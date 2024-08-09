import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_chat(self):
        result = self.app.post('/chat', data=dict(query="What are the course fees for Computer Science?"))
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Computer Science", result.data)

if __name__ == '__main__':
    unittest.main()
