from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add related_name to avoid the reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this to avoid the clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change this to avoid the clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
