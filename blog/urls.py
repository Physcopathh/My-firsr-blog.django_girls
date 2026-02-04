#blog urls
from blog import views
from django.urls import path
from .models import Post
from django.utils import timezone
from django.shortcuts import render

urlpatterns = [
    path('', views.post_list, name='p_l'),
    path('hello/', views.hello, name='hello'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]