from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from mainapp.models import Post

from mainapp.models import MD


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['user', 'category', 'name', 'description', 'posts_text', 'is_active']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['category', 'name', 'description', 'posts_text', 'is_active']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:post_list')
