from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import request
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View

from .models import LoginForm


def index(request):
    return render(request, 'index.html', context={
        'greeting': _('Hello'),
    })


class SignUp(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'sign_up_form.html', context = {})


class Login(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', context = {'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, _('username or password incorrect'))
        
        return render(request, 'login.html', context={})

class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class Users(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by('username')
        users_context = []
        fields = User._meta.get_fields()
        print(fields)
        for user in users:
            users_context.append({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'date_joined': user.date_joined,
                }
            )
        return render(request, 'users.html', context = {'users': users_context})
