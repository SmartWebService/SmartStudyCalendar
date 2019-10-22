from django.shortcuts import render, redirect
from .models import Event
from model_utils.fields import StatusField
from model_utils import Choices
import datetime
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

def input(request) : 
     return render(request, 'inputinfo.html')




def post(request) :
    if request.method == "POST":
        name = request.POST.get("name")
        place = request.POST.get("place")
        Sday = request.POST.get("Sday")
        Eday = request.POST.get("Eday")
        print(request.POST)



                   # hour, min = crawler.calc_time(int(j['end_time']))
                   # e = datetime.time(hour, min, 0)


        Event(owner=request.user, title=name, place=place, start=Sday, end=Eday, is_from_timetable=True).save()
        if request.user.is_authenticated:
            events = Event.objects.filter(owner=request.user).all()
        # print(type(events))
        user_events_json = ""
        for event in events:
            user_events_json += event.toJson()
        # print(user_events_json)
        return render(request, 'my-calendar.html', {'user_events_json': user_events_json})

        # form = PostForm(request.POST)
        # if form.is_valid():
        #     lotto = form.save(commit = False)
        #     lotto.generate()
        # return redirect('connect-everytime')
    else:
        return render(request, "error.html")



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

