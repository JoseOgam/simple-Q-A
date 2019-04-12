from django.shortcuts import render

# Create your views here.

# This is the simplest view possible in Django.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello am Joseph! am teaching myself how to program")
