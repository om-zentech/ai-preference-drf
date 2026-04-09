from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('superadmin', 'SuperAdmin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'superadmin'
        else:
            self.role = 'user'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
    