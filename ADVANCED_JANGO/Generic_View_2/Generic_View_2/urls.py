from django.contrib import admin
from django.urls import path , include
from API import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentListandCreate.as_view()),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),

]
