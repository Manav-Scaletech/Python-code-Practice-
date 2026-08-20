from django.shortcuts import render
from .models import Student
from .seralizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def student_detail(request):
    stu = Student.objects.get(id = 2)
    serializer = StudentSerializer(stu)
    print(type(serializer.data))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    print(type(serializer.data))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
   
