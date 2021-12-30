from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def index(request):

    return render(request, "hello/index.html")
def hamza(request):
    return HttpResponse("Hello, Hamza")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })
def isitchristmas(request):
    date = datetime.date
    status = "No"
    if (date.month==12 and date.day==24):
       status = "Yes"

    return render(request, "hello/christmas.html", {
        "status": status
    })