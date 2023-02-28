from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from .const import SEX_CHOICES

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','password1','password2', 'birth_day', 'sex', 'ailments')
        model = User
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'

