from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *


@api_view(['GET'])
def catalogs_list(request):
    """
 List  catalogs.
 """
    if request.method == 'GET':
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data)
