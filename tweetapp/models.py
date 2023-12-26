from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=100)


    def __str__(self):
        return (f"Username: {self.username}, Message: {self.message}")
