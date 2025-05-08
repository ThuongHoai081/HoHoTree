from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser 
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, fullName,**extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user.set_unusable_password() 
        user = self.model(email=email, fullName=fullName, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, fullName, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, fullName, **extra_fields)

    def create_superuser(self, email, fullName, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        user = self.model(email=email, full_name=fullName, **extra_fields)

class User(AbstractBaseUser):
    username = None 
    first_name = None
    last_name = None
    password = None

    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("full_name"), max_length=150, default="Unknown")
    class Status(models.IntegerChoices):
        PENDING = 0, _('Pending')
        APPROVED = 1, _('Approved')

    status = models.IntegerField(_("status"), choices=Status.choices, default=Status.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]  

    objects = UserManager()

    def __str__(self):
        return self.email
