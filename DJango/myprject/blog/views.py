from django.shortcuts import render
from django.db import models

# Create your views here.
def register(request):
    from .models import post

    all_posts = post.objects.all()
    return render(request, 'blog/index.html')

#custom manager :
class StudentManager(models.Manager):

    def adults(self):
        return self.filter(age__gte=18)