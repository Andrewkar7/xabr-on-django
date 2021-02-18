from django.contrib import admin
from .models import XabrUser


class XabrUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')


admin.site.register(XabrUser, XabrUserAdmin)
