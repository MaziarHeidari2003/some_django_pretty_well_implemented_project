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
  image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=255)
  content = models.TextField()
  counted_views = models.IntegerField(default=0)
  status = models.BooleanField(default=False)
  published_date = models.DateTimeField(null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['created_date']

  def __str__(self):
    return "{} - {}".format(self.title, self.id)
  
  def snippets(self):
    return self.content[:150]


  def get_absolute_url(self):
    return reverse('blog:single', kwargs={'pid':self.id})




class Comments(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  created_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  message = models.TextField()
  subject = models.CharField(max_length=255)
  approve = models.BooleanField(default=True)
  email = models.EmailField()
