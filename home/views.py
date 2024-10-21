from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.contrib import messages


class HomeView(TemplateView):
  template_name = 'home/login.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("hwloo")
            user = form.save()
            login(request, user)
            return redirect('gotonote')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'home/next.html', {'form': form})


def login_view(request):
    home_view = HomeView.as_view()

    if request.method == 'POST':
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gotonote')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()

    return home_view(request)

def logoutvi(request):
    logout(request)
    return redirect('login')