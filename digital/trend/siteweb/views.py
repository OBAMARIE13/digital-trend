from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def blogdetail(request):
    return render(request, 'blog-detail.html')

def projetdetail(request):
    return render(request, 'projet-detail.html')