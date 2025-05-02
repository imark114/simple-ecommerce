from django.urls import path
from .views import (
    UserProfileView,
    ChangePasswordView,
)

urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
] 