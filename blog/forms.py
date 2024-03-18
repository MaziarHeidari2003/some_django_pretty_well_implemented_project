from django import forms
from .models import Comments 
from django.forms import Textarea
from captcha.fields import CaptchaField



class Comment_form(forms.ModelForm):

  class Meta:
    model=Comments
    fields= ['name', 'email', 'subject', 'message','post']
   