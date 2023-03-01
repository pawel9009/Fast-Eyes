from django.contrib import admin
from django.urls import include, path
from . import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('image/', include('app.urls', namespace='app')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
