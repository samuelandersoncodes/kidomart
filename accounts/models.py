from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User model


class MyAccountManager(BaseUserManager):
    """
    This class creates a custom regular user
    and a custom super user
    """

    def create_user(self, first_name, last_name, username, email, password=None):
        # Creates regular user and set mandatory fields for email and username
        if not email:
            raise ValueError('You must have an email')

        if not username:
            raise ValueError('You must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        # Creates super user
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


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
    # Extends MyAccountManager objects
    objects = MyAccountManager()

    def __str__(self):
        # Returns email address value
        return self.email

    def has_perm(self, perm, Obj=None):
        # Mandatory method for permission
        return self.is_admin

    def has_module_perms(self, add_label):
        # Grants module access permissions
        return True


class UserProfile(models.Model):
    # User profile model
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile/')
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=20)

    def __str__(self):
        # First name str representation
        return self.user.first_name

    def full_address(self):
        # Full address concatenation
        return f'{self.address_line_1} {self.address_line_2}'
