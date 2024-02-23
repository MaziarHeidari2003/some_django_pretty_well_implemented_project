from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.blog_view, name='index' ),
  path('<int:pid>', views.blog_single, name='single' ),
  path('<int:pid>', views.detail_post, name='detail_post'),
  path('<int:pid>', views.next_post, name='next_post')

]