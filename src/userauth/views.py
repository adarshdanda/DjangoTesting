from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from forms import CreateUserForm


# Create your views here.
def signup_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

#def signin_view(request)