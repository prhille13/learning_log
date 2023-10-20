"""Defines URL patterns for uses"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]