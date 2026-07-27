from django.db import models

# Create your models here.

class pannel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    objects = StudentManager()

class person(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
