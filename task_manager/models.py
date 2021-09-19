from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class SighUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
