from django.shortcuts import render

def register(request):
    # Register view
    return render(request, 'accounts/register.html')

def login(request):
    # login view
    return render(request, 'accounts/login.html')

def logout(request):
    # logout view
    return