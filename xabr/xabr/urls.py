from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    # path('auth/', include('mainapp.urls', namespace='auth')),
    path('admin/', admin.site.urls),
]
