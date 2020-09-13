from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']
        
        widgets = {
            'username': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs = {
                'class': 'form-control',
                'required': 'True',
            })
        }