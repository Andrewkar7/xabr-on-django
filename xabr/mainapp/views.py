from django.shortcuts import render
from .models import Category, Post


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def post(request, pk):
    context = {
        'page_title': 'хабр',
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

