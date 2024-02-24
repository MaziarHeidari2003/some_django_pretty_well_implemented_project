from django import template
from blog.models import Post,Category

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

@register.inclusion_tag('blog/blog-popular-posts.html')
def popularposts(args=1):
  posts = Post.objects.filter(status=1).order_by('published_date')[:args]
  return {'posts':posts}

@register.inclusion_tag('blog/blog-category.html')
def postcategories():
  posts = Post.objects.filter(status=1) 
  categories = Category.objects.all() 
  cat_dict = {}
  for name in categories:
     cat_dict[name] = posts.filter(category=name).count() 
  return {'categories':cat_dict}   