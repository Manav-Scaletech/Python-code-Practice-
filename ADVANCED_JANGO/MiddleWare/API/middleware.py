import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
       print(f"[{datetime.datetime.now()}]Request URL : {request.path}")


    def process_response(self, request, response):
        pass
        