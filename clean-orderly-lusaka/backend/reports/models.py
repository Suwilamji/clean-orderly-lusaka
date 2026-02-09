import uuid
from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('LITTERING', 'Littering'),
        ('ILLEGAL_PARKING', 'Illegal Parking / Congestion'),
        ('UNAUTHORIZED_VENDING', 'Unauthorized Vending'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    photo = models.ImageField(upload_to='reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category