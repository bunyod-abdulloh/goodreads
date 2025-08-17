from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        user_data = {
            "username": "Bunyod3",
            "password": "bunyod3",
            "first_name": "Bunyod",
            "last_name": "Abdulloh",
            "email": "bunyod0590@gmail.com"
        }
        self.client.post(path=reverse("users:register"), data=user_data)

        user = User.objects.get(username=user_data['username'])

        self.assertEqual(user.first_name, "Bunyod")
        self.assertEqual(user.last_name, "Abdulloh")
        self.assertEqual(user.email, "bunyod0590@gmail.com")
        self.assertTrue(user.check_password("bunyod3"))

    def test_required_fields(self):
        user_data = {
            "first_name": "Bunyod3",
            "email": "bunyod0590@gmail.com"
        }
        response = self.client.post(
            path=reverse("users:register"),
            data=user_data
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)

        self.assertFormError(
            form=response.context['form'],
            field='username',
            errors='This field is required.'
        )
        self.assertFormError(
            form=response.context['form'],
            field='password',
            errors='This field is required.'
        )

    def test_invalid_email(self):
        user_data = {
            "username": "Bunyod3",
            "password": "bunyod3",
            "first_name": "Bunyod",
            "last_name": "Abdulloh",
            "email": "invalid-email"
        }
        response = self.client.post(path=reverse("users:register"), data=user_data)

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)

        self.assertFormError(
            form=response.context['form'],
            field='email',
            errors='Enter a valid email address.'
        )

    def test_unique_username(self):
        first_user_data = {
            "username": "Bunyod3",
            "password": "bunyod3",
            "first_name": "Bunyod",
            "last_name": "Abdulloh",
            "email": "bunyod0590@gmail.com"
        }

        second_user_data = {
            "username": "Bunyod4",
            "password": "bunyod3",
            "first_name": "Bunyod",
            "last_name": "Abdulloh",
            "email": "bunyod_other@gmail.com"
        }

        self.client.post(path=reverse("users:register"), data=first_user_data)
        response = self.client.post(path=reverse("users:register"), data=second_user_data)

        self.assertFormError(
            form=response.context['form'],
            field='username',
            errors='A user with that username already exists.'
        )


