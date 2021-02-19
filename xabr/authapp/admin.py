from django.contrib import admin

from .models import XabrUser


class XabrUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')
    list_editable = ('is_active',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['password'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['avatar'].disabled = True
            form.base_fields['age'].disabled = True
            form.base_fields['email'].disabled = True
            form.base_fields['activation_key'].disabled = True
            form.base_fields['activation_key_expires'].disabled = True
            form.base_fields['like_quantity'].disabled = True
            form.base_fields['is_staff'].disabled = True
            form.base_fields['groups'].disabled = True
            form.base_fields['user_permissions'].disabled = True
        return form


admin.site.register(XabrUser, XabrUserAdmin)
