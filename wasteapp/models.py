from django.db import models
from django.utils import timezone

class Bin(models.Model):
    STATUS_CHOICES = [
        ('ok','OK'),
        ('full','Full'),
        ('reported','Reported')
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fill_percent = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ok')
    last_reported_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.fill_percent}%)"

class CollectionTruck(models.Model):
    name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100, blank=True)
    capacity = models.PositiveIntegerField(default=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CollectionLog(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    truck = models.ForeignKey(CollectionTruck, on_delete=models.SET_NULL, null=True, blank=True)
    collected_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Collected {self.bin.name} by {self.truck or 'N/A'} on {self.collected_at:%Y-%m-%d %H:%M}"
