from rest_framework import serializers
from .models.Product import Product
from .models.Sale import Sale
from .models.Detail_sale import Detail_sale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DetailSaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Detail_sale
        exclude = ('sale',)

class SaleWithDetailsSerializer(serializers.ModelSerializer):
    details = DetailSaleSerializer(many=True, read_only=True, source='detail_sale_set')

    class Meta:
        model = Sale
        fields = ('id', 'total', 'created', 'modified', 'status', 'creator', 'modifier', 'details')
