import random

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
        num_imgs = Image.objects.count()
        random_ids = random.sample(range(1, num_imgs + 1), 10)
        qs = Image.objects.filter(id__in=random_ids)
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
        num_imgs = Image.objects.count()
        random_ids = random.sample(range(1, num_imgs + 1), 20)
        qs = Image.objects.filter(id__in=random_ids)
        return render(request, 'app/challenge.html', {'form': qs})

    def post(self, request, *args, **kwargs):
        if request.POST['labels'] != '':
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

        # faker
        # dur = [500, 5000, 7000]
        # pass_ra = [float(q) for q in range(0,101,10)]
        # for x in range(100):
        #     Experiment.objects.create(user_id=self.request.user,
        #                               pass_rate=pass_ra[random.randint(0,10)],
        #                             samples='sds',
        #                             duration=dur[random.randint(0,2)],
        #                             challenge=False)

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
        
        # faker
        # dur = [500, 5000, 7000]
        # pass_ra = [float(q) for q in range(5,101,5)]
        # for x in range(100):
        #     Experiment.objects.create(user_id=self.request.user,
        #                               pass_rate=pass_ra[random.randint(0,19)],
        #                             samples='sds',
        #                             duration=dur[random.randint(0,2)],
        #                             challenge=True)
        return qs


def upload_images(request):
    """
    In the case of the admin, the ability to
    add all samples to the database
    """

    if request.method == 'GET':
        return render(request, 'app/upload_data.html')

    if request.method == 'POST':
        image_list = request.FILES.getlist('images')

        for img in image_list:
            img_name = str(img).split('.')[0]
            Image.objects.create(img=img, name=img_name)
    return redirect('home')
