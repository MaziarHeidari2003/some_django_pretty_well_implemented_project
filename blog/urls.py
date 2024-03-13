from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.blog_view, name="index"),
  path('<int:pid>', views.blog_single, name='single'),
  path('test',views.test, name='test'),
  path('category/<str:cat_name>', views.blog_view, name='category'),
  path('author/<str:author_username>', views.blog_view, name='author')
]