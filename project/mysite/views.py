from django.shortcuts import render
from django.views import generic


class TestPage(generic.TemplateView):
    template_name = 'test.html'


class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request
        return render(request, self.template_name, {'form': user})
