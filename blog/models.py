from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Post(models.Model):
  category = models.ManyToManyField(Category)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  image = models.ImageField(upload_to='blog', default='blog/default.jpg')
  title = models.CharField(max_length=255)
  content = models.TextField()
  counted_views = models.IntegerField(default=0)
  status = models.BooleanField(default=False)
  published_date = models.DateTimeField(null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['created_date']
    verbose_name = 'پست'
    verbose_name_plural = 'پست ها'

  def __str__(self):
    return self.title  
  
  def snippets(self):
    return self.content[:100] + '...'
  
  '''
  def get_absilute_url(self):
    return reverse('blog:single', kwargs={'pid':self.id})
  '''