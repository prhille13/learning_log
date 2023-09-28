"""Defines URL patterns for lerning_logs"""

from django.urls import path
from . import views

app_name = 'lerning_logs'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]