from django.urls import path
from .views import order_views

urlpatterns = [
    path('', order_views),
]