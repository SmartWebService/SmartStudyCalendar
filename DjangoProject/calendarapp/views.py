from django.shortcuts import render
from .models import Event
from model_utils.fields import StatusField
from model_utils import Choices

# Create your views here.
def intro(reques):
    return render(reques, 'index.html')

def my(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(owner=request.user).all()
        # print(type(events))
        user_events_json = ""
        for event in events:
            user_events_json += event.toJson()
        # print(user_events_json)
        return render(request, 'my-calendar.html', {'user_events_json': user_events_json})
    else:
        return render(request, 'redir.html')