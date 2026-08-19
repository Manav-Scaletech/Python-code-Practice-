from django.shortcuts import render
from.models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication , BasicAuthentication
# from rest_framework.authentication import BasicAuthentication , SessionAuthentication , TokenuAthentication
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser , DjangoModelPermissions , DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]




# generating the tokens 