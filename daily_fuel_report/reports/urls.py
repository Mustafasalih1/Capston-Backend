
from rest_framework.routers import DefaultRouter
from .views import DailyFuelReportViewSet


router = DefaultRouter()
router.register("reports", DailyFuelReportViewSet)

urlpatterns = router.urls
