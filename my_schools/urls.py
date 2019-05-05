"""Defines URL patterns for my_schools."""

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.CatalogList.as_view(), name='catalog'),
]