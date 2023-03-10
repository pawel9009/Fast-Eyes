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
        qs = Image.objects.none()
        unique = []
        self.labels = {}
        while len(unique) < 4:
            random_id = random.randint(1, 12)
            if random_id not in unique:
                unique.append(random_id)
                qs |= Image.objects.filter(id=random_id)

        return render(request, 'app/experiment.html', {'form': qs})

    def post(self, request, *args, **kwargs):
        answers = request.POST['data'][1:].split('-')
        labels = request.POST['labels'][1:].split('-')
        corr_answers = 0
        dict_labels = {name:0 for name in labels}
        
        
        for i, answer in enumerate(answers):
            obj = Image.objects.get(name=labels[i])
            if answer == labels[i]:
                corr_answers += 1
                obj.correct = obj.correct + 1
                dict_labels[labels[i]]=1
                obj.save()
                print('zgadles')
            else:
                obj.incorrect = obj.incorrect + 1
                obj.save()
                print('nie udalo sie', labels[i])
        exp = Experiment.objects.create(user_id=request.user,
                                        pass_rate=round(corr_answers/len(labels)*100, 2),
                                        samples=dict_labels)
        exp.save()
        print(answers)
        print(labels)
        return redirect('home')


# class ImageFormView(TemplateView):
#     form = ImageForm
#     template_name = 'app/exp.html'
#     context_object_name = 'emp'

#     def post(self, request, *args, **kwargs):

#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse_lazy('home', ))
#         context = self.get_context_data(form=form)
#         return self.render_to_response(context)

#     def get(self, request, *args, **kwargs):
#         qs = Image.objects.all().first()
#         return render(request, 'app/exp.html', {'form': qs})


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
        return qs


