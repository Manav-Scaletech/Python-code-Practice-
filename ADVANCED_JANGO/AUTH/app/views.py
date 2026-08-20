from django.shortcuts import render
from.models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser


def home(request):
    """Render the HTML page for the student records in this project."""
    students = Student.objects.order_by('roll', 'name')
    return render(request, 'app/index.html', {'students': students})


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]

# class StudentModelViewset2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]


# class StudentModelViewset3(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
