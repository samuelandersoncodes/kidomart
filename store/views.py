from django.shortcuts import render

def home(request):
    """View for home page"""
    return render(request, 'index.html')