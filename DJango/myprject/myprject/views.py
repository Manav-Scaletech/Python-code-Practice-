from django.http import HttpResponse

def home(request):
    return HttpResponse("it's the home page of the project.")
def about(request):
    return HttpResponse("it's the about page of the project.")
def contact(request):
    return HttpResponse("it's the contact page of the project.")