from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, fullName, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, fullName=fullName, **extra_fields)
        if password: user.password = user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_user(self, email, fullName, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, fullName, password, **extra_fields)

    def create_superuser(self, email, fullName, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, fullName, password, **extra_fields)

class User(AbstractUser):
    username = None 
    first_name = None
    last_name = None

    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("full_name"), max_length=150, default="Unknown")
    status = models.CharField(_("status"), max_length=20, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]  

    objects = UserManager()

    def __str__(self):
        return self.email
