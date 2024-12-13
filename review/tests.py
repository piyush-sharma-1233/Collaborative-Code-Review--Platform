from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        response = self.client.post("/api/auth/signup/", data)  # Use correct path
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        user = User.objects.create_user(username="testuser", password="password123")
        data = {
            "username": "testuser",
            "password": "password123"
        }
        response = self.client.post("/api/auth/login/", data)  # Use correct path
        self.assertEqual(response.status_code, status.HTTP_200_OK)
