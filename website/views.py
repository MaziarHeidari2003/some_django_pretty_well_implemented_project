from django.shortcuts import render
from django.http import HttpResponse
from website.forms import name_forms,contact_form

# Create your views here.


def index_view(request):
  return render(request, 'website/index.html')

def about_view(request):
  return render(request, 'website/about.html')

def contact_view(request):
  if request.method=='POST':
    form = contact_form(request.POST)
    if form.is_valid():
      form.save()
  else:    
    form = contact_form()    
    
  return render(request, 'website/contact.html')

def test_view(request):
  if request.method == 'POST':
    form = contact_form(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('done')
    else:
      return HttpResponse('bitch')
  form = contact_form()
  return render(request, 'website/test.html', {
    'form':form
  })
