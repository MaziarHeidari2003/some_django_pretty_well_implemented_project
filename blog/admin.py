from django.contrib import admin
from blog.models import Post

# Register your models here.

class Post_admin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  empty_value_display = '-emptyBitch-'
  list_display = ('title','author', 'content', 'published_date','created_date')
  ordering = ['created_date']
  search_fields = ['title','content']



admin.site.register(Post,Post_admin)