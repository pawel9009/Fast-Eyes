from django.urls import path
from .views import ImageFormView

app_name = 'app'

urlpatterns = [
    path('', ImageFormView.as_view(), name='image')
]
