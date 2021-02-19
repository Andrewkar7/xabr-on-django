from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import XabrUser


class XabrUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')
    list_editable = ('is_active',)

    def has_change_permission(self, request, obj=None):
        obj = XabrUser.objects.filter(is_active=True)
        if obj:
            return True
        return False

admin.site.register(XabrUser, XabrUserAdmin)
