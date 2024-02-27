from django import forms
from website.models import Contact,news_letter


class name_forms(forms.Form):
  name = forms.CharField(max_length=255)
  email = forms.EmailField()
  subject = forms.CharField(max_length=255)
  message = forms.CharField(widget=forms.Textarea)


class contact_form(forms.ModelForm):
  class Meta:
    model= Contact
    fields = '__all__'


class news_letter_form(forms.ModelForm):

  class Meta:
    model = news_letter
    fields = '__all__'
