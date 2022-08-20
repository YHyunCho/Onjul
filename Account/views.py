from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def signup(request) :
  if request.method == 'POST' :
    if request.POST['password1'] == request.POST['password2'] :
      user = User.objects.create_user(
                                      username=request.POST['username'],
                                      password=request.POST['password1'],
                                      email=request.POST['email'],)
      auth.login(request, user)
      return redirect('login')
    return render(request, 'Account/signup.html')
  return render(request, 'Account/signup.html')

def login(request):
  if request.method == 'POST' :
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None :
      auth.login(request, user)
      return redirect('../../index')
    else :
      return render(request, 'Account/login.html', {'error': 'username or password is incorrect'})
  else :
    return render(request, 'Account/login.html')

def logout(request) :
  auth.logout(request) 
  return redirect('../../index')

def mypage(request) :
  return render(request, 'Account/mypage.html')