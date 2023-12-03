from django import forms
from .models import Account, UserProfile


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
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['tel'].widget.attrs['placeholder'] = 'Enter phone number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        """
        Overrides the clean method to perform additional validation
        Gets cleaned data from the form
        Extracts the password and confirmpassword from cleaned data
        And checks if both passwords match
        If passwords don't match, it raises a validation error
        """
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Sorry! Both passwords must match"
            )


class UserForm(forms.ModelForm):
    # User form
    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'tel'
        )


class UserProfileFrom(forms.ModelForm):
    # User profile from
    class Meta:
        model = UserProfile
        fields = (
            'address_line_1',
            'address_line_2',
            'country',
            'state',
            'city',
            'profile_picture'
        )
