from . models import DailyFuelReport
from .serializers import DailyFuelReportSerializer
from rest_framework import generics


# Create your views here.

class DailyFuelReportListView(generics.ListAPIView):
    queryset = DailyFuelReport.objects.all()
    serializer_class = DailyFuelReportSerializer