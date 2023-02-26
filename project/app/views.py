from django.shortcuts import render
from django.views import generic


class TestPage(generic.TemplateView):
    template_name = 'test.html'


class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'


class HomeView(generic.TemplateView):
    template_name = 'index.html'

# class UserListView(generic.ListView):
#     model = User
#     template_name = 'home.html'


# class UserCreateView(generic.CreateView):
#     model = User