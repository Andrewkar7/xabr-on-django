import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('post/<slug:slug>/', mainapp.post, name='post'),
    path('help/', mainapp.help, name='help'),
    path('category/<slug:slug>/', mainapp.category_page, name='category_page'),
    path('changelike/<slug:slug>/', mainapp.change_like, name='change_like'),
]
