from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, PostAdmin)
admin.site.register(Post, PostAdmin)

