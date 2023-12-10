from django.test import TestCase
from django.contrib.auth import get_user_model


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