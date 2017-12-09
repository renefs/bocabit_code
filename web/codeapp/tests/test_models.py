from django.test import TestCase

# Create your tests here.
from codeapp.models import Tag, Code, Snippet, Project
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


class ProjectTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        Project.objects.create(title="This is the project title",
                                 description="This is the project description",
                                 owner=user)

    def test_project_exist(self):
        project = Project.objects.get(title="This is the project title")
        self.assertNotEqual(project.title, "", "title should not be empty")

    def test_project_not_exist(self):
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(title="This is NOT the project title")


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
