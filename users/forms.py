from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
#from .models import User, Profile
from django.contrib.auth import get_user_model

User = get_user_model()  # Берём кастомную модель пользователя

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'username', 'autocomplete': 'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'password', 'autocomplete': 'current-password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'email', 'autocomplete': 'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'password', 'autocomplete': 'new-password'
    }))
    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact__section-input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'contact__section-input'}))

    class Meta:
        model = User
        fields = ('username', 'email')
