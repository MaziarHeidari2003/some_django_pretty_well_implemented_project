from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='total')
def total_posts():
  posts = Post.objects.all()
  return posts.count()

@register.simple_tag(name='posts')
def posts():
  posts = Post.objects.all()
  return posts

@register.filter
def snippets(value,args=50):
  return value[:args] + '...'