from django.urls import path
from .views import patient_views

urlpatterns = [
    path('', patient_views),
]