from django.test import TestCase

# Create your tests here.
from users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="test@test.com")

    def test_user_exist(self):
        """Animals that can speak are correctly identified"""
        lion = User.objects.get(email="test@test.com")

    def test_user_not_exist(self):
        """Animals that can speak are correctly identified"""
        # lion = User.objects.get(email="test2@test.com")
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email="test2@test.com")
