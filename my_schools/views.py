from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Catalog, Training


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_catalogs = Catalog.objects.all().count()
    num_trainings = Training.objects.all().count()

    context = {
        'num_catalogs': num_catalogs,
        'num_trainings': num_trainings,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def signup(request):
    """view function for signup for training"""
    training = Training.pk

    context = {
        'training': training
    }

    return render(request, 'signup.html', context=context)


class CatalogList(LoginRequiredMixin, generic.ListView):
    model = Catalog


class CatalogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Catalog


class TrainingList(LoginRequiredMixin, generic.ListView):
    model = Training


class TrainingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Training
