from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic.base import View

from .forms import CommentForm
from .models import Category, Post, Comments, Like
from xabr.settings import LOGIN_URL

from authapp.models import XabrUser


def index(request):
    posts = Post.objects.filter(is_active=True).order_by('-create_datetime')
    categories = Category.objects.filter(is_active=True)

    context = {
        'page_title': 'главная',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'mainapp/index.html', context)


def post(request, slug):
    '''вывод полной статьи'''

    posts = Post.objects.filter(slug=slug, is_active=True)
    categories = Category.objects.all()
    comment = Comments.objects.filter(slug=slug)
    #comment = post.comments.filter(active=True)
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = posts              #в этой строке из-за слагов форма комментария не сохраняется
            form.save()
            return redirect(post)
    else:
        form = CommentForm()

    context = {
        'page_title': 'хабр',
        'posts': posts,
        'categories': categories,
        'comments': comment,
        'form': form,
    }
    return render(request, 'mainapp/post.html', context)


def help(request):
    categories = Category.objects.filter(is_active=True)
    context = {
        'page_title': 'помощь',
        'categories': categories
    }
    return render(request, 'mainapp/help.html', context)


def category_page(request, slug):
    categories = Category.objects.filter(is_active=True)
    new_like, created = Like.objects.get_or_create(user=request.user, slug=slug)
    if slug == '':
        category = {'slug': '', 'name': 'все'}
        posts = Post.objects.filter(is_active=True).order_by('-create_datetime')
    else:
        category = get_object_or_404(Category, slug=slug)
        posts = category.post_set.filter(is_active=True).order_by('-create_datetime')

    context = {
        'page_title': 'главная',
        'categories': categories,
        'category': category,
        'posts': posts,
        'new_like': new_like,
    }
    return render(request, 'mainapp/category_page.html', context)



def all_user_posts(request):
    categories = Category.objects.filter(is_active=True)
    posts = Post.objects.filter(user=request.user,is_active=True).order_by('-create_datetime')

    context = {
        'page_title': 'главная',
        'posts': posts,
        'categories': categories,

    }
    return render(request, 'mainapp/all_user_posts.html', context)


def change_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    new_like, created = Like.objects.get_or_create(user=request.user, slug=slug)

    if request.method == 'POST':
        new_like.is_active = not new_like.is_active
        if not new_like.is_active:
            post.like_quantity += 1
            post.save()
            new_like.save()
        else:
            post.like_quantity -= 1
            post.save()
            new_like.save()
        context = {
            'new_like': new_like,
            }

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'), context)







