from django import forms
from .models import registrationmodel

class InputForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.CharField(max_length = 100)
    password = forms.CharField(max_length=100,widget= forms.PasswordInput())

class registration(forms.ModelForm):
    class Meta:
        model = registrationmodel
        fields = "__all__"
