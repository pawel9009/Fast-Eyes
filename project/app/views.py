import random

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from .forms import ExperimentForm, ImageForm
from .models import Experiment, Image


class ExperimentView(TemplateView):
    form = ExperimentForm
    template_name = 'app/experiment.html'

    def get(self, request, *args, **kwargs):
        num_imgs = Image.objects.count()
        random_ids = random.sample(range(1, num_imgs + 1), 5)
        qs = Image.objects.filter(id__in=random_ids)
        return render(request, 'app/experiment.html', {'form': qs})

    def post(self, request, *args, **kwargs):
        answers = request.POST['data'][1:].split('-')
        labels = request.POST['labels'][1:].split('-')
        duration_time = int(request.POST['time'])
        corr_answers = 0
        dict_labels = {name:0 for name in labels}
        
        for i, answer in enumerate(answers):
            obj = Image.objects.get(name=labels[i])
            if answer == labels[i]:
                corr_answers += 1
                obj.correct = obj.correct + 1
                dict_labels[labels[i]]=1
                obj.save()
            else:
                obj.incorrect = obj.incorrect + 1
                obj.save()
        exp = Experiment.objects.create(user_id=request.user,
                                        pass_rate=round(corr_answers/len(labels)*100, 2),
                                        samples=dict_labels,
                                        duration = duration_time)
        exp.save()
        print(answers)
        print(labels)
        return redirect('home')


def upload_images(request):

    if request.method == 'GET':
        return render(request, 'app/upload_data.html')

    if request.method == 'POST':
        image_list = request.FILES.getlist('images')

        for img in image_list:
            name1 = str(img).split('.')[0]
            Image.objects.create(img=img, name=name1)
    return redirect('home')


class ExperimentListView(LoginRequiredMixin, ListView):
    model = Experiment
    template_name = 'app/exp_list.html'
    context_object_name = 'exp_list'

    def get_queryset(self):
        qs = Experiment.objects.filter(user_id=self.request.user)
        qs = qs.order_by('-id')
        return qs


