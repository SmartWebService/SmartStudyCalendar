from django.shortcuts import render, redirect
from .models import Event
from model_utils.fields import StatusField
from model_utils import Choices

# Create your views here.
def intro(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/mycalendar')


def my(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(owner=request.user).all()
        user_events_json = ""
        for event in events:
            user_events_json += event.toJson()
        return render(request, 'my-calendar.html', {'user_events_json': user_events_json, 'df':"""defaultView: 'timeGridWeek',"""})
    else:
        return redirect('/')


def kmu(request):
    events = Event.objects.filter(feed=1).all()
    user_events_json = ""
    for event in events:
        user_events_json += event.toJson()
    return render(request, 'my-calendar.html', {'user_events_json': user_events_json, 'df':''})


def kmusw(request):
    events = Event.objects.filter(feed=2).all()
    user_events_json = ""
    for event in events:
        user_events_json += event.toJson()
    return render(request, 'my-calendar.html', {'user_events_json': user_events_json, 'df':''})

def error(request):
    return render(request, 'error.html')