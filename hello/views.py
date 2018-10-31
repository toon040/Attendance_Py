from django.shortcuts import render

# Create your views here.
import re
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log(request):
    return render(request, "hello/log.html")

def hello_there(request, name):   

       return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )