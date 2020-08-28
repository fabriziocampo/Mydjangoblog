from django.conf.urls import url
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post
#show database content as a list ListView


# post list | home
# single post
# resume
# contact

urlpatterns = [
    url(r'^homepage/$',posts_views.homepage,name="homepage"),
    url(r'^$', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = "list_posts.html", paginate_by = 5),
        name="list"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "single_post.html"), name="single"),
   # url(r'^portfolio/$', posts_views.portfolio, name="portfolio"),
    url(r'^resume/$', posts_views.resume, name="resume"),

    url(r'^contact/$', posts_views.contact, name="contact"),
    
    url(r'^education/$',posts_views.education, name="education"),
    url(r'^contactme/$',posts_views.contactme, name="contactme"),  
    url(r'^projects/$',posts_views.projects,name="projects"), 
    
    url(r'^skills/$', posts_views.skills,name="skills"),
]
