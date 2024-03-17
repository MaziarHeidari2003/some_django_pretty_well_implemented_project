from django.shortcuts import render,redirect
from django.contrib.auth import authenticate


# Create your views here.

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user != None:
      login(request, user)
      return redirect('/')
  
  return render(request, 'accounts/login.html')

def logout(request):
  pass

def signup(request):
  return render(request, 'accounts/signup.html')