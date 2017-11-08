import datetime
from django.test import TestCase

# Create your tests here.
from users.models import User, UserGroup


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="test@test.com")

    def test_user_exist(self):
        User.objects.get(email="test@test.com")

    def test_user_not_exist(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email="test2@test.com")


class UserGroupTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        User.objects.create(email="test2@test.com", username="user2")
        User.objects.create(email="test3@test.com", username="user3")
        UserGroup.objects.create(title="This is a title",
                                 owner=user,
                                 description="This is the group description")

    def test_group_exist(self):
        group = UserGroup.objects.get(title="This is a title")
        self.assertNotEqual(group.uuid, "", "UUID should not be empty")
        self.assertEqual(group.description, "This is the group description", "Description doesn't match")
        self.assertEqual(group.users.count(), 0, "Users must be 0")

        now = datetime.datetime.now()
        self.assertEqual(group.created_at.day, now.day, "Day must be today")
        self.assertEqual(group.created_at.month, now.month, "Month must be today")
        self.assertEqual(group.created_at.year, now.year, "Month must be today")

    def test_group_not_exist(self):
        with self.assertRaises(UserGroup.DoesNotExist):
            UserGroup.objects.get(title="This is a title 2")

    def test_group_users_add(self):
        group = UserGroup.objects.get(title="This is a title")
        user2 = User.objects.get(username="user2")
        user3 = User.objects.get(username="user3")

        group.users.add(user2)
        group.users.add(user3)

        group.save()

        group = UserGroup.objects.get(title="This is a title")
        self.assertEqual(group.users.count(), 2, "Users must be 2")

    def test_group_users_remove(self):
        group = UserGroup.objects.get(title="This is a title")
        user2 = User.objects.get(username="user2")
        user3 = User.objects.get(username="user3")

        group.users.add(user2)
        group.users.add(user3)

        group.save()

        group = UserGroup.objects.get(title="This is a title")
        self.assertEqual(group.users.count(), 2, "Users must be 2")

        group.users.remove(user2)
        group.save()

        group = UserGroup.objects.get(title="This is a title")
        self.assertEqual(group.users.count(), 1, "Users must be 1")
