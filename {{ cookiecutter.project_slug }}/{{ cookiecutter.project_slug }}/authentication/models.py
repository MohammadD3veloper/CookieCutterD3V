from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    BaseUserManager
)
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from {{ cookiecutter.project_slug }}.core.models import BaseModel


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("User object should has an username field")

        user = self.model(
            username=username,
            **extra_fields
        )

        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, password, **extra_fields)



class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """ Custom user model """

    def upload_image(self, filename):
        return f"users/{self.username}/images/{filename}/"

    username = models.CharField(max_length=30, unique=True, validators=[
        ASCIIUsernameValidator,
        MinLengthValidator(5),
        MaxLengthValidator(30)
    ])
    photo = models.ImageField(upload_to=upload_image)
    about = models.TextField(max_length=500)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin
