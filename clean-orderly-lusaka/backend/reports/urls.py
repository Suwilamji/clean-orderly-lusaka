from django.urls import path
from .views import ReportCreateView, ReportListView  # Changed from .views

urlpatterns = [
    path('reports/', ReportCreateView.as_view(), name='report-create'),
    path('reports/list/', ReportListView.as_view(), name='report-list'),
]