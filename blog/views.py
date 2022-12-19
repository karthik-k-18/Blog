from django.shortcuts import render
# import http response
from django.http import  Http404,HttpResponseRedirect
from datetime import date
#import models
from .models import Post, Comment
#import forms
from .forms import CommentForm
#import reverse
from django.urls import reverse


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
    stored_posts = request.session.get("read_later")
    if(stored_posts is None):
        is_added_to_read_later = False
    else:
        if identified_post.id not in stored_posts:
            is_added_to_read_later = False
        else:
            is_added_to_read_later = True
    if request.method == "GET":
        return render(request, "blog/post-detail.html", {
            "post": identified_post,
            "comments": comments,
            "comment_form": CommentForm(),
            "is_added_to_read_later": is_added_to_read_later

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
                "message": "Your comment has been added!",
                "is_added_to_read_later": is_added_to_read_later
            })
        else:
            return render(request, "blog/post-detail.html", {
                "post": identified_post,
                "comment_form": form,
                "comments": comments,
                "message": "Your comment was not added. Please try again.",
                "is_added_to_read_later": is_added_to_read_later
            })
    else:
        return Http404()

def read_later(request):

    if request.method=="POST":
        post_id=int(request.POST.get("post-id"))
        if request.session.get("read_later") is None:
            request.session["read_later"] = list()
        else:
            if post_id not in request.session.get("read_later"):
                request.session["read_later"].append(post_id)
            else:
                request.session["read_later"].remove(post_id)
        #save the session
        request.session.modified = True
        return HttpResponseRedirect(reverse("all_posts"))
        
    else:
        stored_posts = list()
        # print(request.session.get("read_later"))
        if request.session.get("read_later") is None:
            stored_posts = list()
        else:
            for post_id in request.session.get("read_later"):
                stored_posts.append(Post.objects.get(id=post_id))
        return render(request, "blog/read-later.html", {
            "posts": stored_posts,
        })