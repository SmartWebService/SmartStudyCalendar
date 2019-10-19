from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
import json

# Create your models here.
class Event(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, default='')
    place = models.CharField(max_length=100, default='')
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_from_timetable = models.BooleanField(default=False)

    def toJson(self):
        result = """{id: """ + str(self.id) + """, title: '""" + self.title + """',start: '""" + str(self.start.isoformat())[:19] + """',end: '"""+ str(self.end.isoformat())[:19] + """'},"""

        return result
    
    def __str__(self):
        return self.title