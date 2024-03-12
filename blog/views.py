from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

def blog_view(request):
  posts = Post.objects.filter(status=1)
  return render(request, 'blog/blog-home.html',{
    'posts':posts
  })


def blog_single(request,pid):
  post = get_object_or_404(Post,pk=pid)
  return render(request, 'blog/blog-single.html', {
    'post':post
  })

def test(request):
  return render(request, 'blog/test.html')