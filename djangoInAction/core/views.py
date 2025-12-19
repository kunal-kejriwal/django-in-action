from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def core_home(request):
    return HttpResponse("Welcome to the Core Application of Django-In-Action project.")

def first_view(request):
    return HttpResponse("This is the first view added, in the CORE app.")