from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic.base import View

from .forms import CommentForm
from .models import Category, Post, Comments
from xabr.settings import LOGIN_URL

from authapp.models import XabrUser


def index(request):
    posts = Post.objects.all().order_by('-create_datetime')
    categories = Category.objects.all()

    context = {
        'page_title': 'главная',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'mainapp/index.html', context)



def post(request, slug):
    '''вывод полной статьи'''

    posts = Post.objects.filter(slug=slug)
    categories = Category.objects.all()
    comment = Comments.objects.filter(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = posts          #в этой строке из-за слагов форма комментария не сохраняется
            form.save()
            return redirect(post, slug)
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
    categories = Category.objects.all()
    context = {
        'page_title': 'помощь',
        'categories': categories
    }
    return render(request, 'mainapp/help.html', context)


def category_page(request, slug):
    categories = Category.objects.all()
    if slug == '':
        category = {'slug': '', 'name': 'все'}
        posts = Post.objects.all().order_by('-create_datetime')
    else:
        category = get_object_or_404(Category, slug=slug)
        posts = category.post_set.order_by('-create_datetime')

    context = {
        'page_title': 'главная',
        'categories': categories,
        'category': category,
        'posts': posts,
    }
    return render(request, 'mainapp/category_page.html', context)



def all_user_posts(request):
    categories = Category.objects.all()

    posts = Post.objects.filter(user=request.user).order_by('-create_datetime')


    context = {
        'page_title': 'главная',
        'posts': posts,
        'categories': categories,

    }
    return render(request, 'mainapp/all_user_posts.html', context)


def change_like(request, slug):

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.is_active = not post.is_active         # попыпка прописать выключатель активности лайка,пока не получилоась
        if post.is_active:
            post.like_quantity += 1
            post.save()
        else:
            post.like_quantity -= 1
            post.save()
        #return HttpResponseRedirect(reverse('mainapp/post.html'))


    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp/post.html', kwargs={'slug': slug}))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




