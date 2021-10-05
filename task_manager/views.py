from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.urls.base import reverse_lazy
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import UpdateView

from .forms import UserCreationWithEmailForm, UserUpdateForm


def index(request):
    return render(request, 'index.html', context={
        'greeting': _('Hello'),
    })


class SignupUserView(View):

    def get(self, request):
        form = UserCreationWithEmailForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationWithEmailForm(request.POST)
        if not form.is_valid():
            return render(request, 'registration/signup.html', {'form': form})
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')


class LoginUserView(LoginView):
    def get_success_url(self):
        return reverse('/')


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/update.html'
    success_url = reverse_lazy('/')


    def get(self, request, user_id):
        if not user_id == request.user.id:
            messages.error(self.request, 'Вы не можете изменять других пользователей')
            return redirect('users')
        return super(UpdateView, self).get(self, request)


    def get_object(self):
        user = get_object_or_404(User, id=self.kwargs['user_id'])
        return user


class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by('username')
        users_context = []
        fields = User._meta.get_fields()
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
