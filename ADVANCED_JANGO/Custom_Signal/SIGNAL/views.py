from django.shortcuts import render , HttpResponse 
from SIGNAL import signals

# Create your views here.
def home(request):
    signals.notification.send(sender = None , request = request , user = ['custom' , 'signals'])
    return HttpResponse("here is the home page that you are looking for")