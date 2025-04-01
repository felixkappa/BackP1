from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class FormComment(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    

class FormContact(forms.Form):
    full_name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()