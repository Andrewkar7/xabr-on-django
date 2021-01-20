from django.shortcuts import render
from .models import Category, Post


def index(request):
    posts = Post.objects.all().order_by('-create_datetime')
    context = {
        'page_title': 'главная',
        'posts': posts,
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


def design(request):
    context = {
        'page_title': 'дизайн',
    }
    return render(request, 'mainapp/design.html', context)


def web_development(request):
    context = {
        'page_title': 'веб-разработка',
    }
    return render(request, 'mainapp/web-development.html', context)


def mobile_development(request):
    context = {
        'page_title': 'мобильная-разработка',
    }
    return render(request, 'mainapp/mobile-development.html', context)


def marketing(request):
    context = {
        'page_title': 'маркетинг',
    }
    return render(request, 'mainapp/marketing.html', context)

