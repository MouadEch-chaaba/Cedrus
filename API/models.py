from cgi import maxlen

from django.db import models


# Create your models here.

class Idea(models.Model):
    idea_text = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(default=None)
