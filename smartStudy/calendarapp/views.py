from django.shortcuts import render
from .models import Event
from model_utils.fields import StatusField
from model_utils import Choices

# Create your views here.
def my(request):
    events = Event.objects.filter(owner=request.user)
    print(type(events))


    return render(request, 'my-calendar.html')