from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import HomeView


# Name for the application along with paths some of which require login
app_name = 'statistic'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='plot'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
