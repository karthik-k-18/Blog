from django.shortcuts import render
# import http response
from django.http import  Http404
from datetime import date
#import models
from .models import Post, Comment
#import forms
from .forms import CommentForm


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
    comments=identified_post.comments.all().order_by("-date")
    if request.method == "GET":
        return render(request, "blog/post-detail.html", {
            "post": identified_post,
            "comments": comments,
            "comment_form": CommentForm()
        })
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                comment=form.cleaned_data["comment"],
                post=identified_post
            )
            new_comment.save()
            return render(request, "blog/post-detail.html", {
                "post": identified_post,
                "comment_form": CommentForm(),
                "comments": comments,
                "message": "Your comment has been added!"
            })
        else:
            return render(request, "blog/post-detail.html", {
                "post": identified_post,
                "comment_form": form,
                "comments": comments,
                "message": "Your comment was not added. Please try again."
            })
    else:
        return Http404()
