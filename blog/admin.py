from django.contrib import admin

# Register your models here.

from .models import Author, Tag, Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'tags', 'date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('date',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'date')
    list_filter = ('post', 'date')
    search_fields = ('name',)
    ordering = ('date',)

admin.site.register(Author)
admin.site.register(Tag) 
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)