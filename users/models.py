from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STATE_CHOICES = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    
    state = models.CharField(max_length=100, choices=STATE_CHOICES, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return "{} : {}".format(self.state, self.username)