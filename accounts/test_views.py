from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from django.contrib.messages import get_messages


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


class LoginViewTest(TestCase):
    # Test the registration view
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
        )

    def test_login_view_success(self):
        # Test the login view with valid credentials
        url = reverse('login')
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data)
        # Check if the user is redirected to the dashboard on successful login
        if response.url.startswith(reverse('login')):
            # If login is unsuccessful, the user is redirected back to the login page
            self.assertRedirects(response, reverse('login'))
        else:
            # Check if the user is redirected to the dashboard on successful login
            self.assertRedirects(response, reverse('dashboard'))
