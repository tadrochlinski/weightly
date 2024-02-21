from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from .models import UserProfile


def landing_page_view(request):
    return render(request, 'landing_page/index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(
                user=user,
                gender=form.cleaned_data['gender'],
                current_weight=form.cleaned_data['current_weight'],
                height=form.cleaned_data['height'],
                age=form.cleaned_data['age'],
                lifestyle=form.cleaned_data['lifestyle'],
                goal=form.cleaned_data['goal']
            )

            login(request, user)
            return redirect('landing_page')
    else:
        form = RegisterUserForm()

    return render(request, 'landing_page/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginUserForm()

    return render(request, 'landing_page/login.html', {'form': form})

