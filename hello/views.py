from django.shortcuts import render

# Create your views here.
import re
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView

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

def log_message(request):
    if request.method == "POST":
        form = LogMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        form = LogMessageForm()
        return render(request, "hello/log_message.html", {"form": form}) 