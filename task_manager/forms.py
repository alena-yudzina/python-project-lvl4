from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ( EmailField)
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = _('Username')
        self.fields['username'].widget.attrs.update({'placeholder':''})

        self.fields['password'].label = _('Password')
        self.fields['password'].widget.attrs.update({'placeholder':''})


class UserCreationWithEmailForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for key in self.fields.keys():
            self.fields[key].widget.attrs.update({'placeholder':''})


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
       super(UserChangeForm, self).__init__(*args, **kwargs)
       del self.fields['password']