import unittest
import json
from app import create_app, db
from app.models import Student, Moderator

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.student_data = {
            'username': 'test_student',
            'password': 'password123',
            'email': 'test@student.com'
        }
        self.moderator_data = {
            'moderator_id': 'test_moderator',
            'associated_university': 'Test University',
            'permissions': 'admin'
        }
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_student_registration(self):
        res = self.client.post('/register/student', data=self.student_data)
        result = json.loads(res.data)
        self.assertEqual(result['message'], 'Student registered successfully')
        self.assertEqual(res.status_code, 201)

    def test_student_login(self):
        res = self.client.post('/register/student', data=self.student_data)
        res = self.client.post('/login/student', data=self.student_data)
        result = json.loads(res.data)
        self.assertIn('access_token', result)
        self.assertEqual(res.status_code, 200)

    def test_moderator_registration(self):
        res = self.client.post('/register/moderator', data=self.moderator_data)
        result = json.loads(res.data)
        self.assertEqual(result['message'], 'Moderator registered successfully')
        self.assertEqual(res.status_code, 201)

    def test_moderator_login(self):
        res = self.client.post('/register/moderator', data=self.moderator_data)
        res = self.client.post('/login/moderator', data=self.moderator_data)
        result = json.loads(res.data)
        self.assertIn('access_token', result)
        self.assertEqual(res.status_code, 200)

    # More tests can be added here for logout, unauthorized access, etc.

if __name__ == '__main__':
    unittest.main()

