from django.urls import path
from .views import ImageFormView,UploadView

app_name = 'app'

urlpatterns = [
    path('', ImageFormView.as_view(), name='image'),
    path('data/', UploadView.as_view(), name='data'),
]
