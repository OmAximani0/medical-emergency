from django.urls import path
from .views import LocationView

urlpatterns = [
    path('add/', LocationView.as_view())
]