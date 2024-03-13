from django import template
from blog.models import Post,Category

register = template.Library()


@register.simple_tag()
def hello():
  posts = Post.objects.filter(status=1)
  return posts

@register.filter
def snippet(value,args=100):
  return value[:args]

@register.inclusion_tag('blog/popular-post.html')
def popularposts():
  posts = Post.objects.filter(status=1).order_by("published_date")
  return {
    "posts":posts
  }


@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
  posts = Post.objects.filter(status=1)
  categories = Category.objects.all()
  cat_dict = {}
  for name in categories:
    cat_dict[name] = posts.filter(category=name).count()
    
  return {
    'categories': cat_dict
  }
