from django.shortcuts import render
# import http response
from django.http import HttpResponse
from datetime import date
#import models
from .models import Post, Author, Tag

# Create your views here.


posts=Post.objects.all()

def few_posts(request):
    # get latest 3 posts in a list sorted on date
    latest_posts = sorted(posts, key=lambda t: t.date, reverse=True)[:3]
    # pass the list to the template
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": posts
    })


def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
