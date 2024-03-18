from django.contrib import admin
from blog.models import Post,Category,Comments

# Register your models here.

class Post_admin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  empty_value_display = '-emptyBitch-'
  list_display = ('title','author','published_date','created_date')
  ordering = ['created_date']
  search_fields = ['title','content']


class Comments_admin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  empty_value_display = '-emptyBitch-'
  list_display = ('name','post','created_date')
  ordering = ['created_date']
  search_fields = ['name','post']


admin.site.register(Post,Post_admin)
admin.site.register(Category)
admin.site.register(Comments, Comments_admin)
