from django.contrib import admin

# Register your models here.

from .models import Author, Tag, Post

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)