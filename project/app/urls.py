from django.urls import path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

from .views import ExperimentView, upload_images, ExperimentListView, ChallengeView,ChallengeListView,ResultsListView

app_name = 'app'

urlpatterns = [
    path('data/', login_required(upload_images), name='data'),
    path('experiment/', login_required(ExperimentView.as_view()), name='experiment'),
    path('challenge/', login_required(ChallengeView.as_view()), name='challenge'),
    path('list/', login_required(ExperimentListView.as_view()), name='list'),
    path('exp_list/', login_required(ExperimentListView.as_view()), name='exp_list'),
    path('chall_list/', login_required(ChallengeListView.as_view()), name='chall_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
