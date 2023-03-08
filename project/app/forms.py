from django import forms

from .models import Image, Experiment


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'img']


class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['user_id', 'samples']
