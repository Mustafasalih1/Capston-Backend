from django.urls import path
from .views import UserListView
from .views_auth import LoginView, LogoutView


urlpatterns = [
    path("users/", UserListView.as_view(), name = "user-list"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
]
