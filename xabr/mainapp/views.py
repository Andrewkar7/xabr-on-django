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
