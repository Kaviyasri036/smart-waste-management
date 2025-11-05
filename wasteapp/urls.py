from django.urls import path
from . import views

app_name = 'wasteapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report_bin, name='report_bin'),
    path('bins/', views.bin_list, name='bin_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assign/', views.assign_truck, name='assign_truck'),
    path('collect/<int:bin_id>/', views.collect_bin, name='collect_bin'),
    path('api/report/', views.api_report_bin, name='api_report_bin'),
    #path('api/bins-data/', views.api_bins_data, name='api_bins_data'),
]
