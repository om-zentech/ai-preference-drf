from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('superadmin', 'SuperAdmin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    is_deleted = models.BooleanField(default=False)
    
    # def save(self, *args, **kwargs):
    #     if self.is_superuser:
    #         self.role = 'superadmin'
    #     else:
    #         self.role = 'user'
    #     super().save(*args, **kwargs)
        
    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()
    
    def __str__(self):
        return self.username
    