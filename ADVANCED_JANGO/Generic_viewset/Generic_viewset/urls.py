from django.contrib import admin
from django.urls import path , include
from API import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('studentapi', views.StudentCreate, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentList.as_view()),
    # path('student/create/', views.StudentCreate.as_view()),
    path('student/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('student/<int:pk>/update/', views.StudentUpdate.as_view()),
    # path('student/<int:pk>/delete/', views.StudentDestroy.as_view()),
]
