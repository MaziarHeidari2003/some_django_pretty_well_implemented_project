from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
  if not request.user.is_authenticated:
    if request.method =='POST':
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request,user)
          return redirect('/')
      
    form = AuthenticationForm()
    return render(request,'accounts/login.html',{
      'form':form
    })
  
  else:
    return redirect('/')



def signup_view(request):
  return render('accounts/signup.html')


@login_required
def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('/')  

  return render(request,'accounts/login.html')