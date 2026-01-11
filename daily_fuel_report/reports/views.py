from . models import DailyFuelReport
from .serializers import DailyFuelReportSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from users.permissions import IsAdminOrSupervisor


# Create your views here.

class DailyFuelReportViewSet(ModelViewSet):
    queryset = DailyFuelReport.objects.all()
    serializer_class = DailyFuelReportSerializer
    permission_classes = [IsAdminOrSupervisor]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)