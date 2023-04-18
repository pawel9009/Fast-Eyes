from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2', 'birth_year', 'sex', 'ailments')
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['ailments'].label = 'Diseases'
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None

        
        self.fields['password2'].help_text = None
        self.fields['ailments'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 50})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': ''})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ''})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ''})
        self.fields['ailments'].widget = forms.TextInput(attrs={'placeholder': ''})

