from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import (
    get_user_model, login, logout
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
            return redirect('/user/check')
        else:
            return render(request, "login.html", {'form': form})
    else:
        return render(request, "login.html", {'form': form})


@login_required(login_url='/user/login')
def logout_user(request):
    form = UserLoginForm()
    logout(request)
    return render(request, "login.html", {'form': form})


@login_required(login_url='/user/login')
def dashboard_check(request):
    return HttpResponse('dashboard')
