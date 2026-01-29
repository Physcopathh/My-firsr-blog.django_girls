#blog urls
from blog import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='p_l'),
    path('hello/', views.hello, name='hello')
]