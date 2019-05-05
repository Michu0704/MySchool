"""Defines URL patterns for my_schools."""

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]