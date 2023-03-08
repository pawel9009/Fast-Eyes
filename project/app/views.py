from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import ImageForm, ExperimentForm
from .models import Image, Experiment

import random



class ExperimentView(TemplateView):
    form = ExperimentForm
    template_name = 'app/experiment.html'
    context_object_name = 'emp'

    def get(self, request, *args, **kwargs):
        qs = Image.objects.none()
        unique = []
        self.labels = {}
        while len(unique)<9:
            random_id = random.randint(1,12)
            if random_id not in unique:
                unique.append(random_id)
                qs |= Image.objects.filter(id=random_id)

        return render(request, 'app/experiment.html', {'form': qs })
    

    def post(self, request, *args, **kwargs):
        answers = request.POST['data'][1:].split('-')
        labels = request.POST['labels'][1:].split('-')
        corr_answers = 0
        for i, answer in enumerate(answers):
            obj = Image.objects.get(name = labels[i])
            if answer == labels[i]:
                corr_answers += 1
                obj.correct = obj.correct + 1
                obj.save()
                print('zgadles')
            else:
                obj.incorrect = obj.incorrect + 1
                obj.save()
                print('nie udalo sie', labels[i])
        exp = Experiment.objects.create(user_id=request.user,
        pass_rate=round(corr_answers/len(labels)*100,2),
        samples=labels)
        exp.save()
   
        print(answers)
        print(labels)
      
 
        return redirect('home')
        



class ImageFormView(TemplateView):
    form = ImageForm
    template_name = 'app/exp.html'
    context_object_name = 'emp'

    def post(self, request, *args, **kwargs):

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home', ))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        qs = Image.objects.all().first()
        return render(request, 'app/exp.html', {'form': qs})

def upload_images(request):

    if request.method == 'GET':
        return render(request, 'app/upload_data.html')

    if request.method == 'POST':
        image_list = request.FILES.getlist('images')

        for img in image_list:
            name1 = str(img).split('.')[0]
            Image.objects.create(img=img, name=name1)
    return redirect('home')
