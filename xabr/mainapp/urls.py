from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('post/<int:pk>/', mainapp.post, name='post'),
    path('help/', mainapp.help, name='help'),
    path('design/', mainapp.design, name='design'),
    path('web_development/', mainapp.web_development, name='web_development'),

]
