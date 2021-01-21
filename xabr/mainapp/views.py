from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def index(request):
    posts = Post.objects.all().order_by('-create_datetime')
    categories = Category.objects.all()

    context = {
        'page_title': 'главная',
        'posts': posts,
        'categories': categories,
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


    categories = Category.objects.all()

    if pk == '0':
        category = {'pk': 0, 'name': 'все'}
        posts = Post.objects.all().order_by('-create_datetime')
    else:
        category = get_object_or_404(Category, pk=pk)
        posts = category.post_set.order_by('-create_datetime')

    context = {
        'page_title': 'главная',
        'categories': categories,
        'category': category,
        'posts': posts,
    }
    return render(request, 'mainapp/category_page.html', context)
