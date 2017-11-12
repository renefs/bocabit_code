from django.test import TestCase

# Create your tests here.
from codeapp.models import Tag, Code
from users.models import User


class TagRelationshipTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        Tag.objects.create(title="This is the tag title",
                           owner=user)

    def test_tag_with_user(self):
        user = User.objects.get(email="test@test.com")
        self.assertEqual(user.owned_tags.count(), 1, "Tags must be 1")


class CodeRelationshipTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        Code.objects.create(title="This is the code title",
                            owner=user,
                            description="This is the description of the Code", )

    def test_code_with_user(self):
        user = User.objects.get(email="test@test.com")
        self.assertEqual(user.owned_codes.count(), 1, "Codes must be 1")

