from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def hello(a):
  posts = Post.objects.filter(status=1).count()
  return posts

