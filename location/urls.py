from django.urls import path
from .views import AddLocationView, AllLocationView

urlpatterns = [
    path('add/', AddLocationView.as_view()),
    path('all/', AllLocationView.as_view()),
]