from django.shortcuts import render

def register(request):
    # Register view
    return render(request, 'accounts/register.html')