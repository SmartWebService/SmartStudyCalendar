from django.shortcuts import render

# Create your views here.
def my(request):
    return render(request, 'my-calendar.html')