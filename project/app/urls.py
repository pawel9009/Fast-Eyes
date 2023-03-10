from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ExperimentView, upload_images, ExperimentListView

app_name = 'app'

urlpatterns = [
    path('data/', upload_images, name='data'),
    path('experiment/', ExperimentView.as_view(), name='experiment'),
    path('list/', ExperimentListView.as_view(), name='exp_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
