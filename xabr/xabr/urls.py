from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import mainapp
from xabr import settings

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('blog/', include('blogapp.urls', namespace='blogapp')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
