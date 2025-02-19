from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> This is blog home page</h1>")

def login(request):
    return HttpResponse("This is login route of blog")

def about(req):
    return HttpResponse("<h2>This is about page of blog<h2>")
