from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context={'name':'arjun','age':23}
    return render(request,'home.html',context)

def add(request):
    context={'name':'gokul'}
    return render(request,'add.html',context)

def view(request):
    return render(request,'view.html')