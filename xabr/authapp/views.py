from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from authapp.forms import XabrUserLoginForm
from django.contrib import auth
from django.urls import reverse
from authapp.forms import XabrUserRegisterForm, XabrUserEditForm
from authapp.models import XabrUser


def login(request):
    title = 'вход'
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    login_form = XabrUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main:index'))

    content = {'title': title, 'form': login_form, 'next': next, }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = XabrUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = XabrUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


@login_required
def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = XabrUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        edit_form = XabrUserEditForm(instance=request.user)

    content = {
        'title': title,
        'edit_form': edit_form,
    }

    return render(request, 'authapp/edit.html', content)


@login_required
def read(request):
    user = XabrUser.objects.all()
    title = 'профиль пользователя'

    content = {
        'title': title,
        'user': user,
    }

    return render(request, 'authapp/read.html', content)
