from django.contrib import admin
from .models import *
# Register your models here.

class postAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  empty_value_display = '_empty_'
  list_display = ('title','author','counted_views', 'status')
  list_filter = ('status','author')
  search_fields = ['content','title']


admin.site.register(Post, postAdmin)
admin.site.register(Category)