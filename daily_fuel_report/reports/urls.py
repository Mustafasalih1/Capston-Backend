from django.urls import path
from .views import DailyFuelReportListView

urlpatterns = [
    path("reports/", DailyFuelReportListView.as_view(), name = "report-list"),
]
