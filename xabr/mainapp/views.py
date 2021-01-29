from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CommentForm
from .models import Category, Post
from xabr.settings import LOGIN_URL



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
    posts = Post.objects.filter(slug=slug)
    categories = Category.objects.all()
    context = {
        'page_title': 'хабр',
        'posts': posts,
        'categories': categories
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


def change_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    #if request.method == 'POST':
        #post.is_active = not post.is_active             # попыпка прописать выключатель активности лайка,пока не получилоась
        #post.like_quantity += 1
        #post.save()
        #return HttpResponseRedirect(reverse('mainapp/post.html'))
    post.like_quantity += 1
    post.save()

    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp/post.html', kwargs={'slug': slug}))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             create_datetime=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'mainapp/post.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})
