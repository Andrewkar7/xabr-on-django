from django.shortcuts import render
from .models import Category, Post


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def post(request, pk):
    posts = Post.objects.filter(pk=pk)
    context = {
        'page_title': 'хабр',
        'posts': posts
    }
    return render(request, 'mainapp/post.html', context)


def help(request):
    context = {
        'page_title': 'помощь',
    }
    return render(request, 'mainapp/help.html', context)

