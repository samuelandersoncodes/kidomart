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

    def __init__(self, *args, **kwargs):
        # Assign form control class and placeholders to fields
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
            self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
            self.fields['tel'].widget.attrs['placeholder'] = 'Enter phone number'
            self.fields[field].widget.attrs['class'] = 'form-control'
