from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.functions
def index(request):
    return HttpResponse('<h1 style="color:red">index page</h1')

def about(request):
    return HttpResponse('<h1 style="color:blue">about page</h1')