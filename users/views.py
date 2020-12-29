from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Upload
from .forms import CreateUserForm
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user.get_username()
        uploads = Upload.objects.filter(uploader__username=user)
        context = {'uploads' : uploads}
        
        return render(request,'index.html', context)

    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                # print("user created")
                return redirect('login')
        
        context = {'form':form}
        return render(request, 'register.html', context)



def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == 'POST':
            # grabing the username and password to authenticate user
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("A valid login request was made")
                login(request, user)
                return redirect('index')

            else:
                print("a user failed to login")
                messages.info(request, 'Username OR password is incorrect')
        
        return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('index')