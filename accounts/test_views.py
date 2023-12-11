from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth import get_user_model
from .forms import RegistrationForm


class RegisterViewTest(TestCase):
    # Test the registration view
    def test_register_view(self):
        # Define test data
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'tel': '1234567890',
            'password': 'testpassword',
        }

        # Make a POST request to the register view with the test data
        response = self.client.post(reverse('register'), data)
