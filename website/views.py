from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Contact
from .forms import Name_forms,Contact_form,Newsletter_form
from django.contrib import messages


# Create your views here.


def index_view(request):
  return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
   if request.method =='POST':
      form = Contact_form(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request,messages.SUCCESS, 'your ticket submmited succesfully')
      else:
         messages.add_message(request,messages.ERROR, 'your ticket didnt submit')    
   


   form = Contact_form()      
   return render(request,'website/contact.html', {
      'form':form

   })


def newsletter_view(request):
  if request.method == 'POST':
    form = Newsletter_form(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
   
  else:
      return HttpResponseRedirect('/')   



def test(request):
  if request.method == 'POST':
     form = Contact_form(request.POST)
     if form.is_valid():
      form.save()
     else:
        return HttpResponse('asshole')

  form = Contact_form()  
  return render(request, 'website/test.html', {
      'form':form
  })