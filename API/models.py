from cgi import maxlen

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Idea(models.Model):
    idea_text = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(default=None)


class User(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
