from django import forms
from .models import *
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.forms import ModelForm, TextInput, Select, RadioSelect

PAYMENT_CHOICES = (
    ('paystack', 'Paystack'),
    ('flutterwave', 'Flutterwave'),
    ('PayOnDelivery', 'PayOnDelivery'),
)

class SubscriptionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Blake Sandra', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'blakesandra@example.com', 'class':'form-control'}))
    to = forms. EmailField()

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '6, Bode Thomas Street', 'class': 'form-control d-block w-100'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or Suite', 'class': 'form-control d-block w-100'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    zip_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control d-block w-100'
    }))
    
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)