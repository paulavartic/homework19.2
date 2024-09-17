from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    avatar = models.ImageField(
        verbose_name='Avatar',
        help_text='Add your photo',
        null=True,
        blank=True,
        upload_to='users/avatars/',
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name='Phone number',
        help_text='Fill in your phone number',
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=50,
        verbose_name='Country',
        help_text='Where are you from?',
        blank=True,
        null=True,

    )
    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
