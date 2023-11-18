from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    # Registration form
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password'
    }))

    class Meta:
        # Gets specified fields into form
        model = Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'tel',
            'password'
        ]
