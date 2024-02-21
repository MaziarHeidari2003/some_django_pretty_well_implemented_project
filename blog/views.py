from django.shortcuts import render, get_object_or_404
from .models import *
from datetime import datetime

# Create your views here.


def blog_view(request):
  posts = Post.objects.filter(
    published_date = datetime.now()
  )
  return render(request, 'blog/blog-home.html', {
    'posts': posts
  })

def blog_single(request):
  return render(request, 'blog/blog-single.html')

def test(request,pid):
  post = get_object_or_404(Post,pk=pid)
  return render(request, 'blog/test.html',{
    'post': post
  })

