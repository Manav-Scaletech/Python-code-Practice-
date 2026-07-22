from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def new(request):
    return HttpResponse("here is the new page ")

def newone(request):
    return HttpResponse("anothere one project")

def home_page(request):
    return HttpResponse("<h1>Welcome to the home page</h1>")


class Myclassview(View):
    def get(self,request):
        return HttpResponse("<h1>Welcome to the class based view example of it.</h1>")
    
class Mynameclass(View):
    name = "Manav"
    def get(self,request):
        return HttpResponse(f"my name is {self.name}")

