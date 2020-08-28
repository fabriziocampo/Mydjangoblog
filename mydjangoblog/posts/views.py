from django.shortcuts import render

# Create your views here.

def homepage(request):
	return render(request, "homepage.html")

def single_post(request):
    return render(request, "single_post.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
	return render(request, "resume.html")

def education(request):
	return render(request, "education.html")

def contactme(request):
	return render(request, "contactme.html")

def projects(request):
	return render(request, "projects.html")

def skills(request):
	return render(request, "skills.html")