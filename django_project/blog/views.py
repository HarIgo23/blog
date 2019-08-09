from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    # by default
    # <app>/<model>_<viewtype>.html
    # blog/Post_list.html
    template_name = 'blog/home.html'
    # by default
    # name is 'object'
    context_object_name = 'posts'
    # без минуса ASC, с минусом DESC
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
