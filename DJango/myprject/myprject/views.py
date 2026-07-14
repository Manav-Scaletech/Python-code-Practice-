from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("it's the home page of the project.")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("it's the about page of the project.")
def contact(request):
    return HttpResponse("it's the contact page of the project.")