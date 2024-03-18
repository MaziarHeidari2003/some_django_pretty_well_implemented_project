from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def login_view(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      form = AuthenticationForm(request=request, data=request.POST)
      if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user != None:
          login(request, user)
          return redirect('/')
    
    return render(request, 'accounts/login.html')
  
  else:
    return redirect('/')
  

@login_required
def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect('/')
  



def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('accounts:login'))
    else:
      print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')

  form = UserCreationForm()
  return render(request, 'accounts/signup.html', {
    'form':form
  })