from django.contrib import admin
from .models import Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, PostAdmin)
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)

