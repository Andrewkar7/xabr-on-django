from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('post/<int:pk>/', mainapp.post, name='post'),
    path('help/', mainapp.help, name='help'),
    path('category/<int:pk>/page/', mainapp.category_page, name='category_page'),
]
