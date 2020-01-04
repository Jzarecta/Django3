from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("<h1>This is our home page</h1>")

def Sport(request):
    return HttpResponse("<h1>This is our latest Sport news</h1>")

def contact(request):
    return HttpResponse('<h1>This is our contact form</h1>')
