from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def register(request):
    """
    Handles user registration
    It validates the registration form, creates a new user account,
    and saves it to the database if the form is valid.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.tel = tel
            user.save()
            messages.success(request, 'Your Kido Registration is Successful!')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    """
    This function handles user login based on provided email and password.
    And authenticates the user using the provided email and password
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = email.split("@")[0]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'You are logged in as {username}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    # logout view
    auth.logout(request)
    messages.success(request, 'You just logged out!')
    return redirect('login')
