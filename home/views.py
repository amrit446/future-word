from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserRegistration
from .models import User 





# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method=='POST':
        fm=UserRegistration(request.POST)
        if fm.is_valid():
            
            fm.save()
            fm=UserRegistration()
        
    else:
        fm=UserRegistration()
        stud=User.objects.all()
        #user=User.objects.all()
    return render(request, 'signup.html', {'form':fm})
    



def userdetail(request):
    
    stud=User.objects.all()
    #return render(request, 'userdetail.html')
    return render(request, 'userdetail.html', {'stu':stud})


def update_data(request, id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm=UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        
        pi=User.objects.get(pk=id)
        fm=UserRegistration(instance=pi)

    return render(request, 'update.html', {'form':fm})




def del_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/userdetail')
        
    