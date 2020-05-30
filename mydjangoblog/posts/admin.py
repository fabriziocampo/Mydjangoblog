from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date"]
    lists_filter = ["date"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)