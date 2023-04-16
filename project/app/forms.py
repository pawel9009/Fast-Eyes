from django import forms

from .models import Experiment, Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name']


class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['user_id', 'samples']
