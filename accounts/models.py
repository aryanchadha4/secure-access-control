from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('guest', 'Guest'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


from django.db import models
from django.contrib.auth.models import User

class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_accessed = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} accessed {self.view_accessed} at {self.timestamp}"
