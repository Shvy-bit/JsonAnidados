from django.db import models
from django.contrib.auth.models import User

import uuid
class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    total = models.DecimalField(null=False, max_digits=7, decimal_places=2)

    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    status = models.BooleanField(default=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    modifier = models.IntegerField(null=True, blank=True)