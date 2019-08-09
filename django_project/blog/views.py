from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


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


class PostCreateView(LoginRequiredMixin, CreateView):
    # by default need <app>/<model>_form.html template
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # by default need <app>/<model>_form.html template
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # use reverse get error
    # https://stackoverflow.com/questions/31275574/
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
