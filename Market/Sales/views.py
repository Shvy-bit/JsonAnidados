from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from Sales.models.Sale import Sale  
from Sales.serializers import SaleWithDetailsSerializer

class SaleWithDetailsViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().prefetch_related('detail_sale_set__product')
    serializer_class = SaleWithDetailsSerializer
    permission_classes = [AllowAny]