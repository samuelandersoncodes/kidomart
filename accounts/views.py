from django.shortcuts import render
from .forms import RegistrationForm


def register(request):
    # Register view
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    # login view
    return render(request, 'accounts/login.html')


def logout(request):
    # logout view
    return
