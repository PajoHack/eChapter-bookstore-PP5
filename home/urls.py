from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trigger_403/', views.trigger_403_error, name='trigger_403'),
]
