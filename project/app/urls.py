from django.urls import path

from .views import ExperimentView, ImageFormView, upload_images

app_name = 'app'

urlpatterns = [
    path('', ImageFormView.as_view(), name='image'),
    path('data/', upload_images, name='data'),
    path('experiment/', ExperimentView.as_view(), name='experiment'),
]
