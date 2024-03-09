from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.index_view ),
  path('about', views.about_view),
  path('contact', views.contact_view)
]