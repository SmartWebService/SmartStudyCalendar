from django.db import models

# Create your models here.
class Events(models.Model):
    # owner = 
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    url = models.URLField()