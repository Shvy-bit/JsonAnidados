from django.db import models
from django.contrib.auth.models import User
from .Sale import Sale
from .Product import Product

import uuid
class Detail_sale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(null=False, default=1)
    price_unit = models.DecimalField(editable=False, blank=True , max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(editable=False, blank=True, max_digits=7, decimal_places=2)

    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    status = models.BooleanField(default=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    modifier = models.IntegerField(null=True, blank=True)

    def save(self,*args, **kwargs):
        self.price_unit = self.product.price_sale
        self.subtotal = self.price_unit * self.amount
        super().save(*args, **kwargs)
        self.sale.update_total()
    def delete(self, *args, **kwargs):
        sale = self.sale
        super().delete(*args, **kwargs)
        sale.update_total()
    def __str__(self):
        return f"Venta {self.sale.id} - {self.amount} unidades de {self.product.name} | {self.subtotal}"