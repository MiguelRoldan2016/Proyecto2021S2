from django.db import models
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager, models.Manager):
    # Modelo que representa la administracion de los usuarios
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')

        try:
            validate_email(email)
        except ValidationError as e:
            raise ValueError('Email incorrecto', e)

        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False,
            **extra_fields
        )

    def create_staffuser(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=False,
            **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    nombres = models.CharField(max_length=100, default="nombres")
    apellidos = models.CharField(max_length=100, default="apellidos")
    edad = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to=settings.USER_PROFILE_PICS,
                             default=settings.STATIC_URL+'default.png')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return f'{self.apellidos}, {self.nombres}'

    def get_short_name(self):
        return self.email
