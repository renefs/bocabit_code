from django.contrib.auth import authenticate
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from codeapp.models import Code
from users.models import User


class CodeViewsTestCase(TestCase):
    client = None

    def login_user(self):
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True,
                                        is_superuser=True)
        self.user.set_password('hello')
        self.user.save()
        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')
        self.assertTrue(login)

    def logout_user(self):
        self.client.logout()

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_home_not_logged_in_reverse(self):
        # Simple get
        response = self.client.get(reverse('codeapp:code_list'))
        self.assertEqual(response.status_code, 302)

    def test_home_not_logged_in(self):
        # Simple get
        response = self.client.get(reverse('codeapp:code_list'))
        self.assertEqual(response.status_code, 302)

    def test_home_logged_in(self):
        self.login_user()

        response = self.client.get(reverse('codeapp:code_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_code_not_logged(self):
        response = self.client.get(reverse('codeapp:code_create'))
        self.assertEqual(response.status_code, 302)

    def test_create_code_reachable(self):
        self.login_user()

        response = self.client.get(reverse('codeapp:code_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_code(self):
        self.login_user()

        response = self.client.post(reverse('codeapp:code_create'))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(Code.objects.all()), 0)

        response = self.client.post(reverse('codeapp:code_create'), data={'title': 'Example title',
                                                                          'description': "This is a description for the Code"})
        self.assertEqual(response.status_code, 302)

        self.assertEqual(len(Code.objects.all()), 1)

    def test_edit_code_reachable(self):
        self.login_user()

        response = self.client.post(reverse('codeapp:code_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Code.objects.all()), 0)
        response = self.client.post(reverse('codeapp:code_create'), data={'title': 'Example title',
                                                                          'description': "This is a description for the Code"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Code.objects.all()), 1)

        response = self.client.get(reverse('codeapp:code_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(Code.objects.all()), 0)
        # response = self.client.post(reverse('codeapp:code_create'), data={'title': 'Example title',
        #                                                                   'description': "This is a description for the Code"})
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(len(Code.objects.all()), 1)

    def test_edit_code_not_logged(self):
        self.login_user()

        response = self.client.post(reverse('codeapp:code_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Code.objects.all()), 0)
        response = self.client.post(reverse('codeapp:code_create'), data={'title': 'Example title',
                                                                          'description': "This is a description for the Code"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Code.objects.all()), 1)

        self.logout_user()

        response = self.client.get(reverse('codeapp:code_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_edit_code(self):
        self.login_user()

        response = self.client.post(reverse('codeapp:code_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Code.objects.all()), 0)
        response = self.client.post(reverse('codeapp:code_create'), data={'title': 'Example title',
                                                                          'description': "This is a description for the Code"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Code.objects.all()), 1)

        response = self.client.post(reverse('codeapp:code_update', kwargs={'pk': 1}),
                                    data={'title': 'Example NEW title',
                                          'description': "This is the NEW description for the Code"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Code.objects.all()), 1)

        code = Code.objects.get(title="Example NEW title")
        self.assertEqual(code.title, "Example NEW title", "Title must match")
