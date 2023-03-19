import random

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from .forms import ExperimentForm
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
        return redirect('home')
    
    


class ChallengeView(ExperimentView):
    template_name = 'app/challenge.html'

    def get(self, request, *args, **kwargs):
        num_imgs = Image.objects.count()
        random_ids = random.sample(range(1, num_imgs + 1), 20)
        qs = Image.objects.filter(id__in=random_ids)
        return render(request, 'app/challenge.html', {'form': qs})
    

    def post(self, request, *args, **kwargs):
            answers = request.POST['data'][1:].split('-')
            labels = request.POST['labels'][1:].split('-')
            duration_time = int(request.POST['time'])
            
            corr_answers = 0
            
            for i, answer in enumerate(answers):
                obj = Image.objects.get(name=labels[i])
                corr_answers += 1
                obj.correct = obj.correct + 1
                obj.save()

            exp = Experiment.objects.create(user_id=request.user,
                                            pass_rate=round(corr_answers/20, 2),
                                            samples=labels,
                                            duration = duration_time,
                                            challenge = True)
            exp.save()
            return redirect('home')

class ResultsListView(LoginRequiredMixin, TemplateView):
    template_name = 'app/result_list.html'


class ExperimentListView(LoginRequiredMixin, ListView):
    model = Experiment
    template_name = 'app/exp_list.html'
    context_object_name = 'exp_list'

    def get_queryset(self):
        qs = Experiment.objects.filter(user_id=self.request.user, challenge=False)
        qs = qs.order_by('-id')
        return qs


class ChallengeListView(LoginRequiredMixin, ListView):
    model = Experiment
    template_name = 'app/challenge_list.html'
    context_object_name = 'challenge_list'

    def get_queryset(self):
        qs = Experiment.objects.filter(user_id=self.request.user, challenge=True)
        qs = qs.order_by('-id')
        return qs

def upload_images(request):

    if request.method == 'GET':
        return render(request, 'app/upload_data.html')

    if request.method == 'POST':
        image_list = request.FILES.getlist('images')

        for img in image_list:
            name1 = str(img).split('.')[0]
            Image.objects.create(img=img, name=name1)
    return redirect('home')


