from django.shortcuts import render
from django.views import generic


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


class CatalogList(generic.ListView):
    model = Catalog


class CatalogDetailView(generic.DetailView):
    model = Catalog


class TrainingList(generic.ListView):
    model = Training


class TrainingDetailView(generic.DetailView):
    model = Training
