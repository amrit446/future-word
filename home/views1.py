from home.views import userdetail
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 

def loginuser(request):

    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username='email', password='password')
        if user is not None:
            login(request, user)
            print(username, password)
            return render(redirect, '.userdetail.html')
            

        else:
            return render(redirect, 'index.html')
        
            
    return render(request, 'login.html')

    