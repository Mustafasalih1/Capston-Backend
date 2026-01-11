from rest_framework import generics
from .serializers import SiteSerializer,StateSerializer
from .models import State,Site


# Initial list views


class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    
class SiteListView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer