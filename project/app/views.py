from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ImageForm
from .models import Image
import os


class ImageFormView(TemplateView):
    form = ImageForm
    template_name = 'app/exp.html'
    context_object_name = 'emp'

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        qs = Image.objects.all().first()
        
        return render(request, 'app/exp.html', {'form': qs})
    


class UploadView(TemplateView):
    form = Image
    template_name = 'app/upload_data.html'

    def post(self, request, *args, **kwargs):
        context = {}
        context['form'] = self.form
        
        print(context['form'])

        path = 'D:/Github/Fast-Eyes/project/media'
        for filename in os.listdir(path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                name = filename.split('.')[0]
                obj = Image.objects.create(name=name, img = f'{path}/{filename}')
                obj.save()
        print('cos poszlo')
            
        return redirect('home')
