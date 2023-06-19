from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2')
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None

        
        self.fields['password2'].help_text = None
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': ''})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ''})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ''})
 

