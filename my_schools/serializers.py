from rest_framework import serializers
from .models import Catalog


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ('pk', 'name', 'limit', 'provider', 'level')