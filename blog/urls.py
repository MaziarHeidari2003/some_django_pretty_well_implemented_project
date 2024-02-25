from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.blog_view, name='index' ),
  path('<int:pid>', views.blog_single, name='single' ),
  path('<int:pid>', views.detail_post, name='detail_post'),
  path('category/<str:cat_name>', views.blog_view, name='category'),
  path('author/<str:author_username>', views.blog_view, name='author'),
  path('search/',views.blog_search, name='search')


]

