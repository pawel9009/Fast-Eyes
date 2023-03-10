from django.urls import path

from .views import ExperimentView, upload_images, ExperimentListView

app_name = 'app'

urlpatterns = [
    path('data/', upload_images, name='data'),
    path('experiment/', ExperimentView.as_view(), name='experiment'),
    path('list/', ExperimentListView.as_view(), name='exp_list'),
]
