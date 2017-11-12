from django.test import TestCase
from django.test import Client


class UserViewsTestCase(TestCase):
    client = None

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_home(self):
        # Simple get
        # response = self.client.get(reverse('home'))
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
