from rest_framework import serializers
from .models import Report  # 

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report  # Changed from IssueReport
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')