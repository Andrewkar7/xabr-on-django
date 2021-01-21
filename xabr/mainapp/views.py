from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def get_menu():
    print(Category.objects.all())
    return Category.objects.all()

def index(request):
    context = {
        'page_title': 'главная',
        'categories': get_menu(),
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


def category_page(request, pk):

    if pk == '0':
        category = {'pk': 0, 'name': 'все'}
    else:
        category = get_object_or_404(Category, pk=pk)


    context = {
        'page_title': 'главная',
        'categories': get_menu(),
        'category': category,
    }
    return render(request, 'mainapp/category_page.html', context)
