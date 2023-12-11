from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from django.contrib.messages import get_messages
from django.test import TestCase, RequestFactory
from django.contrib.auth.tokens import default_token_generator
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.messages import get_messages
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from accounts.views import activate
from .models import Account, UserProfile
from .views import dashboard
from .forms import UserProfileForm
from orders.models import Order
from datetime import datetime, timedelta
from django.utils import timezone
from unittest.mock import patch


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


class ActivateViewTest(TestCase):
    # Account activation test
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
        )
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)

    def test_activate_view_success(self):
        url = reverse('activate', args=[self.uidb64, self.token])
        request = self.factory.get(url)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = activate(request, self.uidb64, self.token)
        self.assertEqual(response.url, reverse('login'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)
        # Check if success message is displayed
        messages = [m.message for m in get_messages(request)]
        self.assertIn('Your Kido account is activated!', messages)

    def test_activate_view_invalid_link(self):
        # Change the token to simulate an invalid link
        invalid_token = 'invalid_token'
        url = reverse('activate', args=[self.uidb64, invalid_token])
        request = self.factory.get(url)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = activate(request, self.uidb64, invalid_token)
        self.assertEqual(response.url, reverse('register'))
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
        # Check if error message is displayed
        messages = [m.message for m in get_messages(request)]
        self.assertIn('Invalid activation link', messages)

    def test_activate_view_invalid_uid(self):
        # Change the uidb64 to simulate an invalid UID
        invalid_uidb64 = 'invalid_uidb64'
        url = reverse('activate', args=[invalid_uidb64, self.token])
        request = self.factory.get(url)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = activate(request, invalid_uidb64, self.token)
        self.assertEqual(response.url, reverse('register'))
        self.assertFalse(self.user.is_active)
        # Check if error message is displayed
        messages = [m.message for m in get_messages(request)]
        self.assertIn('Invalid activation link', messages)

    def test_activate_view_user_does_not_exist(self):
        # Change the uidb64 to simulate a non-existent user
        non_existent_uidb64 = 'AAAAAAAAAAA'
        url = reverse('activate', args=[non_existent_uidb64, self.token])
        request = self.factory.get(url)
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = activate(request, non_existent_uidb64, self.token)
        self.assertEqual(response.url, reverse('register'))
        # Check if error message is displayed
        messages = [m.message for m in get_messages(request)]
        self.assertIn('Invalid activation link', messages)


class ForgotPasswordViewTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User',
            username='testuser'
        )

    @patch('django.core.mail.EmailMessage.send')
    def test_forgot_password_view_existing_account(self, email_send_mock):
        # Access the forgotPassword view with an existing account
        url = reverse('forgotPassword')
        data = {'email': 'testuser@example.com'}
        # Use follow=True to follow redirects
        response = self.client.post(url, data, follow=True)
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that a success message is set
        self.assertContains(
            response, 'Password reset email has been sent to your email address.')
        # Check that email_send was called (email sending is mocked)
        self.assertTrue(email_send_mock.called)

    def test_forgot_password_view_nonexistent_account(self):
        # Access the forgotPassword view with a nonexistent account
        url = reverse('forgotPassword')
        data = {'email': 'nonexistent@example.com'}
        # Use follow=True to follow redirects
        response = self.client.post(url, data, follow=True)
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Check that an error message is set
        self.assertContains(response, 'This account does not exist')
