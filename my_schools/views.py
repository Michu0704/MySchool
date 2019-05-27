from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F


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
    training = Training.objects.get(pk=7)
    training.participants.add(request.user)
    training.save()

    return render(request, 'signup.html')


class CatalogList(LoginRequiredMixin, generic.ListView):
    model = Catalog


class CatalogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Catalog


class TrainingList(LoginRequiredMixin, generic.ListView):
    model = Training


class TrainingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Training


class TrainingByUser(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing trainings current user takes part in."""
    model = Training
    template_name ='my_schools/users_trainings.html'
    paginate_by = 10

    def get_queryset(self):
        return Training.objects.filter(participants=self.request.user)
