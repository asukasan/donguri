from django.shortcuts import render
from .models import Post, Category, Group

def post_home(request):
    params = {
        "recent_post": Post.objects.order_by('-created_at')[:5],
        "category" :Category.objects.all(),
        "all_post": Post.objects.order_by('-created_at'),
    }
    return render(request, 'post/post_home.html', params)

def post_detail(request, id):
    params = {
        "recent_post": Post.objects.order_by('-created_at')[:5],
        'post': Post.objects.get(id=id),
        "category" :Category.objects.all(),
    }
    return render(request, 'post/post_detail.html', params)

def post_category(request, id):
    params = {
        "recent_post": Post.objects.order_by('-created_at')[:5],
        'post_category': Category.objects.get(id=id),
        "category" :Category.objects.all(),
    }
    return render(request, 'post/post_category.html', params)