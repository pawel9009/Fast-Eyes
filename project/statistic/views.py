from django.shortcuts import render
from django.views import generic
# Create your views here.
from .utils import plot

import matplotlib.pyplot as plt
import pandas as pd
from django.http import HttpResponse
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.template import loader

import base64


class HomeView(generic.TemplateView):
    template_name = 'statistic/home.html'

    def get(self, request, *args, **kwargs):
        img = plot()
        context = {'my_plot': img}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
