from django.shortcuts import render
from django.views import generic
# Create your views here.
from .utils import plot_challenge, plot_experiment
from app.models import Experiment


class HomeView(generic.TemplateView):
    template_name = 'statistic/home.html'

    def get(self, request, *args, **kwargs):
        data_challenge = Experiment.objects.all().filter(challenge=True)
        data_experiment = Experiment.objects.all().filter(challenge=False)

        # context = plot_challenge(data_challenge)
        context = plot_experiment(data_experiment) 
    
        
        return render(request, self.template_name, context)
      
