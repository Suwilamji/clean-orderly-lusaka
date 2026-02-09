from rest_framework import generics
from .models import Report
from .serializers import ReportSerializer
from datetime import timedelta
from django.utils.timezone import now

class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportListView(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        days = int(self.request.query_params.get('days', 7))
        return Report.objects.filter(
            created_at__gte=now() - timedelta(days=days)
        )
