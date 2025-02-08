from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from . forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password =form.cleaned_data['password']
            )
            user.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form=SignupForm()
    return render(request , 'signup.html',{'form':form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username= form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request ,  username=username , password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            form.add_error("Invalid Username or Password!")
    return render(request , 'login.html' , {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request , 'dashboard.html' , {'username':request.user.username})

@login_required
def profile_view(request):
    return render(request , 'profile.html' , {'user':request.user})

@login_required
def change_password_view(request):

    if request.method == 'POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            user=request.user
            if not user.check_password(form.cleaned_data['old_password']):
                form.add_error('old_password',"Old Password is Incorrect!")
            else:
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                return redirect('dashboard')
    else:
        form = ChangePasswordForm()
    return render(request , 'change_password.html' , {'form':form})


