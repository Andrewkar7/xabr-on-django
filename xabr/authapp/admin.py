from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import XabrUser


class XabrUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')
    list_editable = ('is_active',)

    def get_actions(self, request):
        if self.actions is None or IS_POPUP_VAR in request.GET:
            return {}
        actions = self._filter_actions_by_permissions(request, self._get_base_actions())
        return {name: (func, name, desc) for func, name, desc in actions}


admin.site.register(XabrUser, XabrUserAdmin)
