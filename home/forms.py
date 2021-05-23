from django.core import validators
from django import forms
from .models import User


class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email' , 'password', 'confirm_password', 'address']
        widgets={
           'username':forms.TextInput(attrs={'class':'form-control'}),
           'email':forms.EmailInput(attrs={'class':'form-control'}),
           'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
           'confirm_password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
           'address':forms.TextInput(attrs={'class':'form-control'})

        }
        