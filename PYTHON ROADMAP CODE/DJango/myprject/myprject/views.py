from operator import pos
from django.db import models
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
# from requests import post
class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")
    
    def post(self, request):
        # Handle POST requests here
        return HttpResponse("This is a POST request to the Home Page.")
    
def about(request):
    return HttpResponse("it's the about page of the project.")
def contact(request):
    return HttpResponse("it's the contact page of the project.")
def newpath(request):
    return HttpResponse("here is the new path of the website.")





