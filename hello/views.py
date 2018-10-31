from django.shortcuts import render

# Create your views here.
import re
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Hello, Django")

def hello_there(request, name):   

       return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )