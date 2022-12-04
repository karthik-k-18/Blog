from django.contrib import admin

# Register your models here.

from .models import Author, Tag, Post





class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'tags', 'date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('date',)


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)