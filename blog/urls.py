from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.blog_view, name="index"),
  path('single', views.blog_single, name='single'),
  path('<int:pid>',views.test, name='test')
]