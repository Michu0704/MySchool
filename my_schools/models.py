from django.db import models
from django.contrib.auth.models import User


class Catalog(models.Model):
    """
    Catalog of trainings
    Attributes:
        name(str): name of the training
        provider(str): provider of the training
        level(str): difficulty level of the training
    """

    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    def __str__(self):
        """
        Return a string representation of the model.
        """
        return self.name


class Training(models.Model):
    """
    Model of training
    catalog: id of the catalog the training belongs to
    limit(int): limits how many people can take part in training
    auditorium(str): where training takes place
    date: when is the training
    """

    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    limit = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    auditorium = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        """
        Return a string representation of the model
        :return:
        """
        return self.name
