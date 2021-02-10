from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from mainapp.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        qs = Post.objects.filter(is_active=True).order_by('-create_datetime')
        return qs


class DraftListView(ListView):
    model = Post
    template_name = 'post_draft.html'

    def get_queryset(self):
        qs = Post.objects.filter(is_active=False).order_by('-create_datetime')
        return qs


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['user', 'category', 'name', 'slug', 'description', 'posts_text', 'is_active']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['category', 'name', 'slug', 'description', 'posts_text', 'is_active']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:post_list')
