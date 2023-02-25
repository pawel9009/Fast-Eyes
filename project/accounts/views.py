from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from . import forms


class HomeView(generic.TemplateView):
    template_name = 'index.html'

class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'