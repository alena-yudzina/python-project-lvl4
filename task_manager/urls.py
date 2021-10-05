
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from task_manager import views

from .forms import UserLoginForm
from .views import LoginUserView, SignupUserView, UsersView, UserUpdateView

urlpatterns = [
    path('', views.index, name='/'),
    path('admin/', admin.site.urls),
    path('users/create/', SignupUserView.as_view(), name='signup'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:user_id>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:user_id>/delete/', UserUpdateView.as_view(), name='user-delete'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', LoginUserView.as_view(authentication_form=UserLoginForm), name='login'),
]
