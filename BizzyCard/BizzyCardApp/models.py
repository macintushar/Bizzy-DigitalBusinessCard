from django.db import models

# Create your models here.

class CardDetails(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 300)
    designation = models.CharField(max_length = 30)
    
    linkedIn = models.CharField(max_length = 50)
    twitter = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    linkedIn = models.CharField(max_length = 50)