from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import ImageForm
from .models import Image


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
