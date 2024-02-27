from django.contrib import admin
from .models import Contact,news_letter
# Register your models here.


class contact_admin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  list_display = ('name','created_date','email')
  list_filter = ('email',)

admin.site.register(Contact,contact_admin)
admin.site.register(news_letter)