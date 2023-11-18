from django.shortcuts import render
from .forms import RegistrationForm
from .models import Account


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
        else:
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
