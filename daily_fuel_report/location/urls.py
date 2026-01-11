from .views import SiteListView,StateListView
from django.urls import path

urlpatterns = [
    path("sites/", SiteListView.as_view(), name = 'site-list'),
    path("states/", StateListView.as_view(), name = 'state-list'),
    
]
