from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'tel',
            'email',
            'address_line_1',
            'address_line_2',
            'country',
            'state',
            'city',
            'order_note'
        )

    def __init__(self, *args, **kwargs):
        """
        This method adds placeholders and classes,
        remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'tel': 'Phone Number',
            'email': 'Email Address',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'country': 'Country',
            'state': 'State',
            'city': 'City',
            'order_note': 'Leave a Note',
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
