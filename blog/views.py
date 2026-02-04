from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) # Inside of {"String":our_data} we give our data to our template

def hello(request):
    return HttpResponse('<h1>HelloWorld</h1>',)

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/detail.html', {'post':post})
