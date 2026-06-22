from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class Sale(models.Model):

    total = models.DecimalField(editable=False, null=False, default=0.00, blank=True, max_digits=7, decimal_places=2)

    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    status = models.BooleanField(default=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    modifier = models.IntegerField(null=True, blank=True)

    def update_total(self):
        total = self.detail_sale_set.aggregate(total_suma = Sum('subtotal'))['total_suma']
        self.total = total or 0.00
        self.save(update_fields=['total'])
    def __str__(self):
        date = self.created.strftime("%Y-%m-%d - %H:%M")
        return f"Venta {self.id} - Total: {self.total} | ({date})"