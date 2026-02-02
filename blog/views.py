from django.shortcuts import render
import django.http.response as response
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) # Inside of {"String":our_data} we give our data to our template

def hello(request):
    return render(request, 'hello')