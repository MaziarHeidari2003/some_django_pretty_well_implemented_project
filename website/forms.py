from django import forms
from .models import Contact,Newsletter
from django.forms import Textarea

class Name_forms(forms.Form):
  name = forms.CharField(max_length=255)
  email = forms.EmailField(max_length=255)
  subject = forms.CharField(max_length=255)
  message = forms.CharField(widget=forms.Textarea)


class Contact_form(forms.ModelForm):
  class Meta:
    model=Contact
    fields= '__all__'
    widgets = {
      'name': Textarea(attrs= {'cols':80, 'rows':20})
    }


class Newsletter_form(forms.ModelForm):
  class Meta:
    model = Newsletter
    fields = '__all__'    