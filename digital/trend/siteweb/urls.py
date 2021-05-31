from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blogdetail, name='blog-detail'),
    path('projet/detail/', views.projetdetail, name='projet-detail'),

]