from django.test import TestCase, Client
from django.urls import reverse
from .forms import RegistrationForm
from .models import Account

class RegistrationFormTest(TestCase):
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
    
