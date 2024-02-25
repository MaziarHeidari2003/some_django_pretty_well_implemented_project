from django.shortcuts import render, get_object_or_404
from .models import *
from datetime import datetime

# Create your views here.


def blog_view(request,**kwargs):
  posts = Post.objects.filter(status=1)
  if kwargs.get('cat_name') != None:
    posts = posts.filter(category__name=kwargs['cat_name'])
  if kwargs.get('author_username') != None:
    posts = posts.filter(author__username=kwargs['author_username'])

  return render(request, 'blog/blog-home.html', {
    'posts': posts
  })

def blog_single(request, pid):
  posts = Post.objects.filter(status=1)
  post = get_object_or_404(posts,pk=pid )
  return render(request, 'blog/blog-single.html', {
    'post':post
  })

def test(request,pid):
  post = get_object_or_404(Post,pk=pid)
  return render(request, 'blog/test.html',{
    'post': post
  })

def detail_post(request, pid):
  post = Post.objects.get(pk=pid)
  post.counted_views +=1
  post.save()
  posts = Post.objects.all()
  return render(request, 'blog/blog-home.html', {
    'posts': posts
  })



def next_post(request, pid):
  try:
    next_post = Post.objects.get(id>pid)
  except:
    pass
  return render(request, 'blog/blog-home.html',{
    'post': next_post            
  })  


def blog_category(request,cat_name):
  posts = Post.objects.filter(status=1)
  posts = posts.filter(category__name=cat_name)
  return render(request, 'blog/blog-home.html', {
    'posts':posts
  })