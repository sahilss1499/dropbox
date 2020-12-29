from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Upload


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['title', 'file_upload']