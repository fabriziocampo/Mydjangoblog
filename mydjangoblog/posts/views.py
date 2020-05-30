from django.shortcuts import render

# Create your views here.


def single_post(request):
    return render(request, "single_post.html")

def contact(request):
    return render(request, "contact.html")