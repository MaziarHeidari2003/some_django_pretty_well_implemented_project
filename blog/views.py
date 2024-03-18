from django.shortcuts import render
from blog.models import Post, Comments  
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import Comment_form
from django.contrib import messages


# Create your views here.

def blog_view(request, **kwargs):
  posts = Post.objects.filter(status=1)
  if kwargs.get('cat_name') != None:
    posts = posts.filter(category__name=kwargs['cat_name'])
  if kwargs.get('author_username') != None:
    posts = posts.filter(author__username=kwargs['author_username'])  

  posts = Paginator(posts,3)
  try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
  except PageNotAnInteger:
    posts = posts.get_pagec
  except EmptyPage:
    posts = posts.get_page(1)    



  return render(request, 'blog/blog-home.html',{
    'posts':posts
  })


def blog_single(request,pid):
  if request.method == 'POST':
    form = Comment_form(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request,messages.SUCCESS, 'your ticket submmited succesfully')

    else:
        messages.add_message(request,messages.ERROR, 'your ticket submmited succesfully')

  post = get_object_or_404(Post,pk=pid)
  comments = Comments.objects.filter(post=post.id, approve=True).order_by('created_date')
  form = Comment_form()
  return render(request, 'blog/blog-single.html', {
    'post':post,
    'comments':comments,
    'form':form
  })




def test(request):
  return render(request, 'blog/test.html')

def blog_category(request,cat_name):
  posts = Post.objects.filter(status=1)
  posts = posts.filter(category__name=cat_name)
  return render(request, 'blog/blog-home.html',{
    'posts':posts
  })


def blog_search(request):
  posts = Post.objects.filter(status=1)
  if request.method == 'GET':
    if s := request.GET.get('s'):
      posts = posts.filter(content__contains=s)
  
  return render(request, 'blog/blog-home.html',{
    'posts':posts
  })
