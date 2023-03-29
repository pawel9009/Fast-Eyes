from django.shortcuts import render
from django.views import generic

from app.models import Experiment

# Create your views here.
from .utils import plot_challenge, plot_experiment, plot_pie_chart


class HomeView(generic.TemplateView):
    template_name = 'statistic/home.html'

    def get(self, request, *args, **kwargs):
        data_challenge = Experiment.objects.all().filter(challenge=True)
        data_experiment = Experiment.objects.all().filter(challenge=False)
        context = plot_challenge(data_challenge)
        context['exp'] = plot_experiment(data_experiment)
        context['pie_chart'] = plot_pie_chart(data_experiment, data_challenge)
        return render(request, self.template_name, context)
