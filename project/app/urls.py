from django.urls import path

from .views import ExperimentView, ImageFormView, upload_images, ExperimentListView

app_name = 'app'

urlpatterns = [
    path('', ImageFormView.as_view(), name='image'),
    path('data/', upload_images, name='data'),
    path('experiment/', ExperimentView.as_view(), name='experiment'),
    path('list/', ExperimentListView.as_view(), name='exp_list'),
]
