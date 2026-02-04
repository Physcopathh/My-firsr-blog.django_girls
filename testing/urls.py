from django.urls import path
from django.shortcuts import render
from testing import views

urlpatterns = [
    path('helloworld/', views.hello1)
]