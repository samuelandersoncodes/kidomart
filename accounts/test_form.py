from django.test import TestCase, Client
from django.urls import reverse
from .forms import RegistrationForm, UserForm
from .models import Account

class RegistrationFormTest(TestCase):
    # Registration form test
    def setUp(self):
        self.client = Client()

    def test_registration_form_valid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'tel': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123',
        }

        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_passwords(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'tel': '1234567890',
            'password': 'password123',
            'confirm_password': 'differentpassword',
        }

        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Sorry! Both passwords must match', form.errors['__all__'])

    def test_registration_form_submission(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'tel': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123',
        }

        response = self.client.post(reverse('register'), form_data)
        expected_url = reverse('login') + '?command=verification&email=john.doe@example.com'
        self.assertEqual(response.status_code, 302)
    

class UserFormTest(TestCase):
    # User form test
    def setUp(self):
        # Create a user instance for testing
        self.user = Account.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            tel='1234567890',
        )

    def test_user_form_valid_data(self):
        form_data = {
            'first_name': 'UpdatedFirst',
            'last_name': 'UpdatedLast',
            'tel': '9876543210',
        }
        form = UserForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_form_submission_authenticated(self):
        # Log in the user before making the request
        self.client.force_login(self.user)
        form_data = {
            'first_name': 'UpdatedFirst',
            'last_name': 'UpdatedLast',
            'tel': '9876543210',
        }

        response = self.client.post(reverse('edit_profile'), form_data)

    def test_user_form_submission_unauthenticated(self):
        form_data = {
            'first_name': 'UpdatedFirst',
            'last_name': 'UpdatedLast',
            'tel': '9876543210',
        }
        response = self.client.post(reverse('edit_profile'), form_data)
        expected_url = f"{reverse('login')}?next={reverse('edit_profile')}"
        self.assertRedirects(response, expected_url)
