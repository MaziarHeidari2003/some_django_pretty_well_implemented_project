from django import forms
from website.models import Contact


class name_forms(forms.Form):
  name = forms.CharField(max_length=255)
  email = forms.EmailField()
  subject = forms.CharField(max_length=255)
  message = forms.CharField(widget=forms.Textarea)


class contact_form(forms.ModelForm):
  class Meta:
    model= Contact
    fields = '__all__'


