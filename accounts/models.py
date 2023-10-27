from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User model


class Account(AbstractBaseUser):
    """
    This class extends the AbstractBaseUser class
    Represents user accounts
    and includes fields and methods 
    to manage user details and permissions
    """

    # User details
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    tel = models.CharField(max_length=15)
    # Mandatory custom fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    # Set email as username
    USERNAME_FIELD = 'email'
    # Set auth required fields
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        # Returns email address value
        return self.email

    def has_perm(self, perm, Obj=None):
        # Mandatory method for permission
        return self.is_admin

    def has_module_perms(self, add_label):
        # Grants module access permissions
        return True
