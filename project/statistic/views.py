from django.shortcuts import render
from django.views import generic
# Create your views here.
from .utils import plot
from app.models import Experiment


class HomeView(generic.TemplateView):
    template_name = 'statistic/home.html'

    def get(self, request, *args, **kwargs):
        data = Experiment.objects.all().filter(challenge=True)
        
        context = plot(data)
        
        return render(request, self.template_name, context)
      
