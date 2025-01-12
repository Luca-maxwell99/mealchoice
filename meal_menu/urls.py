from django.urls import path
from .views import my_meals

urlpatterns = [
    path('', my_meals,),
]
