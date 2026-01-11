from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Initial list views


class UserListView(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer