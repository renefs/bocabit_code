from django.contrib.auth import authenticate
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from users.models import User


class UserViewsTestCase(TestCase):
    client = None

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_home_not_logged_in_reverse(self):
        # Simple get
        response = self.client.get(reverse('codeapp:index'))
        self.assertEqual(response.status_code, 302)

    def test_home_not_logged_in(self):
        # Simple get
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_home_logged_in(self):
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True,
                                        is_superuser=True)
        self.user.set_password('hello')
        self.user.save()
        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')
        self.assertTrue(login)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
