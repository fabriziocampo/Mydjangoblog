from django.conf.urls import url
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post
#show database content as a list ListView


# post list | home
# single post
# contact

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = "list_posts.html", paginate_by = 5),
        name="list"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "single_post.html"), name="single"),

    url(r'^contact/$', posts_views.contact, name="contact"),
]
