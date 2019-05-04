from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *


@api_view(['GET', 'POST'])
def catalogs_list(request):
    """
 List  catalogs.
 """
    if request.method == 'GET':
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def catalogs_detail(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        catalog = Catalog.objects.get(pk=pk)
    except Catalog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CatalogSerializer(catalog, context={'request': request})
        return Response(serializer.data)
