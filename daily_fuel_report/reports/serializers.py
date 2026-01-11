from rest_framework import serializers
from .models import DailyFuelReport

class DailyFuelReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyFuelReport
        fields = ['site', 'report_date', 'fuel_consumed', 'planned_quantity', 'delivered_quantity', 'remaining_quantity', 'status', 'created_by', 'created_at']
        