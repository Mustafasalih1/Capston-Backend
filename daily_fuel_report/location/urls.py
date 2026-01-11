from rest_framework.routers import DefaultRouter
from .views import StateViewSet, SiteViewSet


router = DefaultRouter()
router.register("states", StateViewSet)
router.register("sites", SiteViewSet)

urlpatterns = router.urls