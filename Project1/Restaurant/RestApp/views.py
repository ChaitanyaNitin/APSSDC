from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'app/home.htm')

def about(request):
    return render(request,'app/about.htm')

def contact(request):
    return render(request,'app/contact.htm')

def login(request):
    return render(request,'app/login.htm') 