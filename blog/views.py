from django.shortcuts import render
import django.http.response as response

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html')#-->for template rendering-

def hello(request):
    return response.HttpResponse('<h1>hello<h1>')