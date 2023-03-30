from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.models import UserCreationForm
from django import forms

def CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'First name', 'Last name', 'password']
