from django.shortcuts import render

# Create your views here.
import re
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Hello, Django")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strptime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    mathch_object = re.match("[a-z or A-Z]",name)

    if mathch_object:
        clean_name = mathch_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's "+ formatted_now
    return HttpResponse(content)