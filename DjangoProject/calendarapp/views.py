from django.shortcuts import render
from .models import Event
from model_utils.fields import StatusField
from model_utils import Choices

# Create your views here.
def my(request):
    events = Event.objects.filter(owner=request.user).all()
    # print(type(events))
    user_events_json = ""
    for event in events:
        user_events_json += event.toJson()
    # print(user_events_json)
    return render(request, 'my-calendar.html', {'user_events_json': user_events_json})