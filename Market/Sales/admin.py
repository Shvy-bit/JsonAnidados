from django.contrib import admin
from .models.Product import Product
from .models.Sale import Sale
from .models.Detail_sale import Detail_sale

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Detail_sale)