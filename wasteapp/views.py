from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.db import models
from django.db.models import Avg
from .models import Bin, CollectionTruck, CollectionLog
from .forms import ReportBinForm
import json
from django.core.serializers import serialize



# 🏠 Home Page
def index(request):
    return render(request, 'wasteapp/index.html')


# 🗑️ Report Bin
def report_bin(request):
    if request.method == 'POST':
        form = ReportBinForm(request.POST)
        if form.is_valid():
            bin_obj = form.save(commit=False)
            bin_obj.status = 'reported' if bin_obj.fill_percent >= 70 else 'ok'
            bin_obj.last_reported_at = timezone.now()
            bin_obj.save()
            return redirect('wasteapp:bin_list')
    else:
        form = ReportBinForm()
    return render(request, 'wasteapp/report_bin.html', {'form': form})


# 📋 Bin List
def bin_list(request):
    bins = Bin.objects.all().order_by('-fill_percent')
    return render(request, 'wasteapp/bin_list.html', {'bins': bins})


# 🟢 Updated Dashboard View (with map support)

def dashboard(request):
    bins = Bin.objects.all()
    trucks = CollectionTruck.objects.all()

    total_bins = bins.count()
    full_bins = bins.filter(fill_percent__gte=90).count()
    reported_bins = bins.filter(status='reported').count()
    avg_fill = round(bins.aggregate(Avg('fill_percent'))['fill_percent__avg'] or 0, 2)

    # ✅ Serialize queryset to JSON for JS
    bins_json = json.loads(serialize('json', bins))
    bins_data = [
        {
            'name': b['fields']['name'],
            'latitude': b['fields']['latitude'],
            'longitude': b['fields']['longitude'],
            'fill_percent': b['fields']['fill_percent'],
            'status': b['fields']['status']
        }
        for b in bins_json
    ]

    context = {
        'bins': bins_data,   # use this for JSON in template
        'total_bins': total_bins,
        'full_bins': full_bins,
        'reported_bins': reported_bins,
        'avg_fill': avg_fill,
        'trucks': trucks,
    }

    return render(request, 'wasteapp/dashboard.html', context)

# 🚛 Updated Assign Truck (for dashboard)
def assign_truck(request):
    if request.method == 'POST':
        bin_id = request.POST.get('bin_id')
        truck_id = request.POST.get('truck_id')

        selected_bin = get_object_or_404(Bin, id=bin_id)
        selected_truck = get_object_or_404(CollectionTruck, id=truck_id)

        CollectionLog.objects.create(
            bin=selected_bin,
            truck=selected_truck,
            collected_at=timezone.now()
        )

        selected_bin.fill_percent = 0
        selected_bin.status = 'ok'
        selected_bin.last_reported_at = timezone.now()
        selected_bin.save()

        return redirect('wasteapp:dashboard')
    return redirect('wasteapp:dashboard')


# 🧹 Manual Bin Collection
def collect_bin(request, bin_id):
    bin_obj = get_object_or_404(Bin, id=bin_id)
    truck = CollectionTruck.objects.filter(active=True).first()
    CollectionLog.objects.create(bin=bin_obj, truck=truck, notes='Collected manually')
    bin_obj.fill_percent = 0
    bin_obj.status = 'ok'
    bin_obj.last_reported_at = timezone.now()
    bin_obj.save()
    return redirect('wasteapp:bin_list')


# 📡 API: Report Bin
@require_POST
def api_report_bin(request):
    name = request.POST.get('name') or request.POST.get('binName')
    location = request.POST.get('location')
    fill_percent = int(request.POST.get('fill_percent') or request.POST.get('fillPercent') or 0)
    lat = request.POST.get('latitude') or None
    lon = request.POST.get('longitude') or None

    bin_obj = Bin.objects.create(
        name=name or f"Bin {timezone.now().strftime('%H%M%S')}",
        location=location or '',
        fill_percent=fill_percent,
        last_reported_at=timezone.now(),
        status='reported' if fill_percent >= 70 else 'ok',
        latitude=lat if lat else None,
        longitude=lon if lon else None
    )
    return JsonResponse({'ok': True, 'id': bin})
