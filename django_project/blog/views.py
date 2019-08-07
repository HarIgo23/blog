from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/dashboard/home.html', context)


def about(request):
    return render(request, 'blog/dashboard/about.html', {'title': 'About'})
