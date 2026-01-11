from rest_framework import serializers
from .models import Site,State

class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = State
        fields = ['state_name']
        
        
class SiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Site
        fields = ['site_name','power_source', 'state', 'capacity', 'status', 'created_at']
