from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
        path('test/', views.TestPage.as_view(), name = 'test'),
        path('thanks/', views.ThanksPage.as_view(), name = 'thanks'),
]