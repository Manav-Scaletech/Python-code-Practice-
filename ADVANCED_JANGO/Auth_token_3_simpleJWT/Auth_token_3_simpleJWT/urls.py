from django.contrib import admin
from django.urls import path , include
from app import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenVerifyView , TokenObtainPairView , TokenRefreshView

router = DefaultRouter()

router.register('studentapi' , views.StudentModelViewset, basename = 'student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('auth' , include('rest_framework.urls')),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
]



# http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="y"

# http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg3MTMzMTY2LCJpYXQiOjE3ODcxMzI4NjYsImp0aSI6IjNlZDM1ZWZjZGM2NTQwY2ViNzc0ODhlNGVhZmQwNjJiIiwidXNlcl9pZCI6IjEifQ.1xpqu0Xbb-AZ5rs1a-hMiglJ9VoCSfN-Z5XoRm0pAgA"

# http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4NzIxOTI2NiwiaWF0IjoxNzg3MTMyODY2LCJqdGkiOiJkZTUzMjJjZDhmMmE0OTBlODUwOWUwNGFiOTIzMGVhYyIsInVzZXJfaWQiOiIxIn0.Bm0vsrQEq-I_Tm9HtWhNNkBN0__dfPnI9fQpdepI9w4" 

# http -f POST http://127.0.0.1:8000/studentapi/ name=Another roll=05 city=mehsana 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg3MTM3NjAxLCJpYXQiOjE3ODcxMzY3MDEsImp0aSI6IjU1YjI4NGNiNzhlYTQ3YWI5ZTE1YTI0MmIwZjA1NGJjIiwidXNlcl9pZCI6IjEifQ.zgR1vIkJk4ZmQGC0s_224gC7QSLhO0ZBoTO4Y9Td0fs'

# superuser password : Scaletech@123