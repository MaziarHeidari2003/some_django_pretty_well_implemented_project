from django.shortcuts import render

# Create your views here.

def login_view(request):
  return render('accounts/login.html')

def signup_view(request):
  return render('accounts/signup.html')