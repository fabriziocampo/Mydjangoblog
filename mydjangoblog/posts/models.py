from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    #now add is setted when file is created,autonow every time we modify something
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    #slug for human friendly urls
    slug = models.SlugField()

    #python 3
    def __str__(self):
        return self.title

    #obtain url of a single post
    def get_absolute_url(self):
        return reverse("single", kwargs={"id": self.id, "slug": self.slug})
