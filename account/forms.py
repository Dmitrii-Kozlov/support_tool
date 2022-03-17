from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import Profile, Airline

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['airline']
        widgets = {
            'airline': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'airline': 'Авиакомпания',
        }