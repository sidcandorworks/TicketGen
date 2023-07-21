# accounts/models.py
from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # Add any additional fields you want for the user (e.g., name, age, etc.)

    def __str__(self):
        return self.email