
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name