from django.shortcuts import render, get_object_or_404
from post.models import Post, Category, Group

def home(request):
    params = {
        "recent_post": Post.objects.order_by('-created_at')[:5],
        "category" :Category.objects.all(),
    }
    return render(request, 'home/home.html', params)


