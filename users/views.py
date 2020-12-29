from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
# Create your views here.

def index(request):
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
    return render(request, 'login.html')