"""Defines URL patterns for my_schools."""

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalogs/', views.CatalogList.as_view(), name='catalog'),
    path('catalog/<int:pk>', views.CatalogDetailView.as_view(), name='catalog-detail'),
    path('trainings/', views.TrainingList.as_view(), name='training'),
    path('training/<int:pk>', views.TrainingDetailView.as_view(), name='training-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('training/signup', views.signup, name='signup-detail'),
    path('mytrainings/', views.TrainingByUser.as_view(), name='my-trainings'),
]