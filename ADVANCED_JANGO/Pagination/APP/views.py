from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 2)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page (page_number)
    return render(request, 'APP/home.html', {'page_obj': page_obj})