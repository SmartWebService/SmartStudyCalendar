from django.db import models
import Users

# Create your models here.
class Blog(models.Model):
    text = models.TextField()

class User(models.Model):
