from django.test import TestCase

# Create your tests here.
from codeapp.models import Tag, Code, Workspace, Snippet
from users.models import User


class TagTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        Tag.objects.create(title="This is the tag title",
                           owner=user)

    def test_tag_exist(self):
        tag = Tag.objects.get(title="This is the tag title")
        self.assertNotEqual(tag.title, "", "title should not be empty")

    def test_tag_not_exist(self):
        with self.assertRaises(Tag.DoesNotExist):
            Tag.objects.get(title="This is NOT the tag title")


class CodeTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        Code.objects.create(title="This is the code title",
                            owner=user,
                            description="This is the description of the Code", )

    def test_code_exist(self):
        code = Code.objects.get(title="This is the code title")
        self.assertNotEqual(code.title, "", "title should not be empty")
        self.assertEqual(code.title, "This is the code title")
        self.assertEqual(code.owner.email, "test@test.com")

    def test_code_not_exist(self):
        with self.assertRaises(Code.DoesNotExist):
            Code.objects.get(title="This is NOT the code title")


class WorkspaceTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        Workspace.objects.create(title="This is the workspace title",
                                 description="This is the workspace description",
                                 owner=user)

    def test_workspace_exist(self):
        workspace = Workspace.objects.get(title="This is the workspace title")
        self.assertNotEqual(workspace.title, "", "title should not be empty")

    def test_workspace_not_exist(self):
        with self.assertRaises(Workspace.DoesNotExist):
            Workspace.objects.get(title="This is NOT the workspace title")


class SnippetTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        code = Code.objects.create(title="This is the code title",
                                   owner=user,
                                   description="This is the description of the Code", )
        Snippet.objects.create(language="python",
                               text="print(\"Hello world!\")",
                               author=user,
                               code=code,
                               title="This is the title")

    def test_base_snippet_exist(self):
        snippet = Snippet.objects.get(id=1)
        self.assertNotEqual(snippet.language, "", "language should not be empty")

    def test_base_snippet_not_exist(self):
        with self.assertRaises(Snippet.DoesNotExist):
            Snippet.objects.get(id=2)
