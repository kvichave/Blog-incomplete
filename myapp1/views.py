from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'base.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html') 
def home(request):
    return render(request, 'home.html') 