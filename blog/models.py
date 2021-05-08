from django.db import models
from django.
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone)
    

