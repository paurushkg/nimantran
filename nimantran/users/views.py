from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import (
    authenticate,
    get_user_model, login
)

User = get_user_model()


@csrf_exempt
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User(
                full_name=form.cleaned_data.get('full_name'),
                email=form.cleaned_data.get('email'),
                phone_number=form.cleaned_data.get('phone_number'),
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponse(user)
        else:
            return render(request, "register.html", {'form': form})
    else:
        return render(request, "register.html", {'form': form})


@csrf_exempt
def login_user(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return HttpResponse('dashboard')
        else:
            return render(request, "login.html", {'form': form})
    else:
        return render(request, "login.html", {'form': form})
