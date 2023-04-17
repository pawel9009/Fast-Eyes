import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView

from .forms import ExperimentForm
from .models import Experiment, Image


class ExperimentView(TemplateView):
    """Experiment view displaying successive samples
      then post creating an object in the database while
        modifying the model of individual samples
    """
    form = ExperimentForm
    template_name = 'app/experiment.html'

    def get(self, request, *args, **kwargs):
        uniq_id = [item.id for item in Image.objects.all()]
        qs= Image.objects.filter(id__in=random.sample(uniq_id, 5))

        return render(request, 'app/experiment.html', {'form': qs})

    def post(self, request, *args, **kwargs):
        
        answers = request.POST['data'][1:].split('-')
        labels = request.POST['labels'][1:].split('-')
        duration_time = int(request.POST['time'])
        corr_answers = 0
        dict_labels = {name: 0 for name in labels}

        for i, answer in enumerate(answers):
            obj = Image.objects.get(name=labels[i])
            if answer == labels[i]:
                corr_answers += 1
                obj.correct = obj.correct + 1
                dict_labels[labels[i]] = 1
                obj.save()
            else:
                obj.incorrect = obj.incorrect + 1
                obj.save()
        exp = Experiment.objects.create(user_id=request.user,
                                        pass_rate=round(corr_answers/len(labels)*100, 2),
                                        samples=dict_labels,
                                        duration=duration_time)
        exp.save()
        return redirect('app:exp_list')


class ChallengeView(ExperimentView):
    """
    Challenege view displaying consecutive samples then posting
    creating an object in the database while modifying the model
    of individual samples depending on the number of responses
    """
    template_name = 'app/challenge.html'

    def get(self, request, *args, **kwargs):
        uniq_id = [item.id for item in Image.objects.all()]
        qs= Image.objects.filter(id__in=random.sample(uniq_id, 20))
        names = ''
        for item in qs:
            names+='-'+item.name
        print(names)
        return render(request, 'app/challenge.html', {'form': qs,'names':names})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if request.POST['labels'] != '/':
            answers = request.POST['data'][1:].split('-')
            labels = request.POST['labels'][1:].split('-')
            duration_time = int(request.POST['time'])
            corr_answers = 0
            for i, _ in enumerate(answers):
                obj = Image.objects.get(name=labels[i])
                corr_answers += 1
                obj.correct = obj.correct + 1
                obj.save()

            exp = Experiment.objects.create(user_id=request.user,
                                            pass_rate=round((corr_answers/20)*100, 2),
                                            samples=labels,
                                            duration=duration_time,
                                            challenge=True)
            exp.save()
            return redirect('app:chall_list')

        return redirect('app:challenge')


class ResultsListView(LoginRequiredMixin, TemplateView):
    """
    Return results where you can choose between 2 options
    """
    template_name = 'app/result_list.html'


class ExperimentListView(LoginRequiredMixin, ListView):
    """
    Return results for ordinary experiments
    """
    model = Experiment
    template_name = 'app/exp_list.html'
    context_object_name = 'exp_list'

    def get_queryset(self):
        qs = Experiment.objects.filter(user_id=self.request.user, challenge=False)
        qs = qs.order_by('-id')
        for item in qs:
            item.samples = item.samples.replace("'", "").replace(",", "").replace("[", "").replace("]", "")
        return qs


class ChallengeListView(LoginRequiredMixin, ListView):
    """
    Return results for challenge
    """
    model = Experiment
    template_name = 'app/challenge_list.html'
    context_object_name = 'challenge_list'

    def get_queryset(self):
        qs = Experiment.objects.filter(user_id=self.request.user, challenge=True)
        qs = qs.order_by('-id')
        for item in qs:
            item.samples = item.samples.replace("'", "").replace(",", "").replace("[", "").replace("]", "")
        return qs


def upload_images(request):
    """
    In the case of the admin, the ability to
    add all samples to the database
    """

    if request.method == 'GET':
        return render(request, 'app/upload_data.html')

    if request.method == 'POST':
        n = 0
        chars = string.ascii_letters + string.digits
        uniq = []
        while n<=500:
            random_string = ''.join(random.choice(chars) for _ in range(5))
            if random_string not in uniq:
                Image.objects.create(name=random_string)
                uniq.append(random_string)
                n+=1
    return redirect('home')
