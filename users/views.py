from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Upload
from .forms import CreateUserForm, UploadForm

from django.contrib.auth.decorators import login_required

# imports for using class based views
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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



@login_required(login_url='login')
def UploadFiles(request):
    form = UploadForm()
    user = request.user.get_username()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)
            upload.uploader = get_object_or_404(User, username=user)
            # data dictionary will contain all the data of the form
            data = form.cleaned_data
            # if there exists an object with the same title previousely then don't save it to the db
            if Upload.objects.filter(uploader=upload.uploader, title=data['title']).exists():
                return HttpResponse('<h1>File with same title exists perviousely upload it with a differnt title</h1>')
                
            upload.file_upload = request.FILES['file_upload']
            upload.save()
            print("Upload Successfull!")
        return redirect('index')


    context = {'form' : form}
    return render(request, 'uploadfile.html', context)
        


    