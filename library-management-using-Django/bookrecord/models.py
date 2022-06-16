from django.db import models
from datetime import datetime 
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=70)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now(), blank=True)