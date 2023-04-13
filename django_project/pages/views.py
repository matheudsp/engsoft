from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(response):
    return HttpResponse("Hello World")


