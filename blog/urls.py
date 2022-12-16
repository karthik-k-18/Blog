#import path
from django.urls import path
from . import views
urlpatterns = [
    path("", views.few_posts, name="few_posts"),
    path("posts",views.all_posts, name="all_posts"),
    path("posts/<slug>",views.post_detail, name="post_detail"),
    path("read-later", views.read_later, name="read-later"),
]
