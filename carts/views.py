from django.shortcuts import render


def cart(request):
    # cart view
    return render(request, 'cart.html')
