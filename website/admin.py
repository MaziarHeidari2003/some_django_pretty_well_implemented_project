from django.contrib import admin
from website.models import Contact 
# Register your models here.

class Contact_admin(admin.ModelAdmin):
  
  list_display =('name','email','created_date')
  list_filter = ('email',)
  search_fields = ('name','message')
  date_hierarchy = 'created_date'
  

admin.site.register(Contact, Contact_admin)
