#blog urls
from blog import views
from django.urls import path
from .models import Post
from django.utils import timezone
from django.shortcuts import render

urlpatterns = [
    path('', views.post_list, name='p_l'),
    path('hello/', views.hello, name='hello'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]