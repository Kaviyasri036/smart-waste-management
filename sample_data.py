# Run this with `python sample_data.py` from project root after migrations are applied.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartwaste.settings')
import django
django.setup()
from wasteapp.models import Bin, CollectionTruck
Bin.objects.create(name='Bin A - Park', location='Central Park', fill_percent=85, status='reported')
Bin.objects.create(name='Bin B - Station', location='Bus Station', fill_percent=45)
Bin.objects.create(name='Bin C - Market', location='Market Road', fill_percent=95, status='reported')
CollectionTruck.objects.create(name='Truck 1', driver_name='Ramu', capacity=2000)
CollectionTruck.objects.create(name='Truck 2', driver_name='Sita', capacity=1500)
print('Sample data created.')
