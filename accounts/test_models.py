from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile


class MyAccountManagerTest(TestCase):
    def test_create_user(self):
        # Get the user model manager
        user_manager = get_user_model().objects

        # Create a regular user
        user = user_manager.create_user(
            first_name='John',
            last_name='Doe',
            username='john_doe',
            email='john@example.com',
            password='testpassword'
        )
        # Assert that the user has the expected attributes
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.username, 'john_doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superadmin)

    def test_create_superuser(self):
        # Get the user model manager
        user_manager = get_user_model().objects
        # Create a superuser
        superuser = user_manager.create_superuser(
            first_name='Admin',
            last_name='User',
            username='admin_user',
            email='admin@example.com',
            password='supersecretpassword'
        )
        # Assert that the superuser has the expected attributes
        self.assertEqual(superuser.first_name, 'Admin')
        self.assertEqual(superuser.last_name, 'User')
        self.assertEqual(superuser.username, 'admin_user')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.check_password('supersecretpassword'))
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superadmin)


class AccountModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
        )

    def test_create_user(self):
        # Retrieve the created user
        user = get_user_model().objects.get(email='test@example.com')

        # Test that the user has the expected attributes
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_superadmin)

    def test_str_representation(self):
        # Test the string representation of the user
        self.assertEqual(str(self.user), 'test@example.com')

    def test_has_perm(self):
        # Test the has_perm method
        self.assertFalse(self.user.has_perm('some_permission'))

    def test_has_module_perms(self):
        # Test the has_module_perms method
        self.assertTrue(self.user.has_module_perms('some_label'))


class UserProfileModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
        )

        # Create a user profile for the test user
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            profile_picture='path/to/image.jpg',
            address_line_1='123 Main St',
            address_line_2='Apt 4',
            country='USA',
            state='NY',
            city='New York',
        )

    def test_create_user_profile(self):
        # Retrieve the created user profile
        user_profile = UserProfile.objects.get(user=self.user)

        # Test that the user profile has the expected attributes
        self.assertEqual(user_profile.user, self.user)
        self.assertEqual(user_profile.profile_picture, 'path/to/image.jpg')
        self.assertEqual(user_profile.address_line_1, '123 Main St')
        self.assertEqual(user_profile.address_line_2, 'Apt 4')
        self.assertEqual(user_profile.country, 'USA')
        self.assertEqual(user_profile.state, 'NY')
        self.assertEqual(user_profile.city, 'New York')

    def test_full_address(self):
        # Test the full_address method
        expected_address = '123 Main St Apt 4'
        self.assertEqual(self.user_profile.full_address(), expected_address)