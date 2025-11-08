from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from uuid import uuid4
from muco_django.utils import UploadByField


class UserManager(BaseUserManager):
    def create_user(self, email, name=None, password=None, logo=None, account_type=None):
        if not email:
            raise ValueError('You must enter a valid email!')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, logo=logo, account_type=account_type)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name=None, password=None):
        user = self.create_user(email=email, name=name, password=password, account_type='usr')
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    ACCOUNT_TYPES = [('br', 'Brand'), ('usr', 'User')]
    account_type = models.CharField(choices=ACCOUNT_TYPES, default='usr')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name