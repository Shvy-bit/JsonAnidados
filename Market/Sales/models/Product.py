from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=True, max_length=50)
    amount = models.IntegerField(null=False, default=1)
    price_buy = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    price_sale = models.DecimalField(null=False, max_digits=6, decimal_places=2)

    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    modifier = models.IntegerField(null=True, blank=True)


    def __str__ (self):
        return "%s %s %s" %(self.id, self.name, self.price_sale)