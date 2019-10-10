from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.
class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    url = models.URLField()

    def toJson(self):
        
        return None