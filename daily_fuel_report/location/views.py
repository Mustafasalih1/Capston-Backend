from rest_framework import generics
from .serializers import SiteSerializer,StateSerializer
from .models import State,Site
from rest_framework.viewsets import ModelViewSet
from users.permissions import IsAdminUserRole

# Initial list views


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAdminUserRole]
    
class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAdminUserRole]